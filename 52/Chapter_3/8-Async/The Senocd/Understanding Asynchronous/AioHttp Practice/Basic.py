# -*- coding: utf-8 -*-
# @Time     :   2020/5/3 0:30
# @Author   :   Payne
# @File     :   Basic.py
# @Software :   PyCharm
from urllib.parse import urljoin
from pyquery import PyQuery as pq
import re
import aiohttp
import asyncio
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# URL = 'https://www.baidu.com'
# URL = 'https://www.lagou.com/'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_CONNECTION_NAME = 'books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_CONNECTION_NAME]

BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10
CONCURRENCY = 5
semaphore = asyncio.Semaphore(CONCURRENCY)


async def scrape(url):
    logging.info('Scraping URL:%s ...', url)
    async with semaphore:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        # print(await response.text())
                        return await response.text()
                    else:
                        logging.info(f'Response Status :{response.status}  Response Messages:{await response.text()}')
        except aiohttp.ClientSession as e:
            logging.info('Error:%s', e, exc_info=True)


async def scape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return await scrape(index_url)


async def scape_datail(url):
    html = await scrape(url)
    return await parse_detail(html)


async def parse_detail(html):
    """
    parse detail page
    :param html: html of detail page
    :return: data
    """
    doc = pq(html)
    cover = doc('img.cover').attr('src')
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


async def main():
    scape_index_tasks = [asyncio.ensure_future(scape_index(page)) for page in range(1, TOTAL_PAGE + 1)]
    results1 = await asyncio.gather(*scape_index_tasks)
    print(results1)
    detail_urls = []
    for result1 in results1:
        if not result1: continue
        doc = pq(result1)
        links = doc('.el-card .name')
        for link in links.items():
            href = link.attr('href')
            detail_urls.append(urljoin(BASE_URL, href))
    logging.info('get detail url %s', detail_urls)
    scrape_detail_tasks = [asyncio.ensure_future(scape_datail(detail_url)) for detail_url in detail_urls]
    data = await asyncio.wait(scrape_detail_tasks)
    print(data)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
