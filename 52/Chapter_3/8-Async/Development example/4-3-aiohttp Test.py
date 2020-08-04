# -*- coding: utf-8 -*-
# @Time     :   2020/4/4 1:29
# @Author   :   Payne
# @File     :   4-3-aiohttp Test.py
# @Software :   PyCharm
import asyncio
import logging
import aiohttp
import json
import time
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# response = requests.get('https://dynamic5.scrape.cuiqingcai.com/')
# print(response.status_code)
# print(response.text)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s:%(message)s')

INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/id={id}'
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 3
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api(url):
    try:
        logging.info('scraping %s', url)
        async with session.get(url) as response:
            return await response.json()
    except aiohttp.ClientError:
        logging.error('Error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, 6)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('Results %s', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))


if __name__ == '__main__':
    start = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    end = time.time()
    print("RUNNING TIME", end - start)
