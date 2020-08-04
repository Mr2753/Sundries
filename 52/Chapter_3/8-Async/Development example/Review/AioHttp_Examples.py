# -*- coding: utf-8 -*-
# @Time     :   2020/4/20 10:27
# @Author   :   Payne
# @File     :   AioHttp_Examples.py
# @Software :   PyCharm
import asyncio
import logging
import json
import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient

'''实现思路'''
'''First'''
# 爬取所有列表页的异步爬取、可以将所有的列表页的爬取任务集合起来
# 声明为Task组成的列表进行异步爬取
'''Second'''
# 拿到上一步列表页的所有内容并解析,拿到所有书的ID信息
# 组合为所有详情页的爬取任务集合,声明为task组成的列表,进行异步爬取
# 同时爬取的结果也以异步的方式存储到MongoDB中


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s:%(message)s')
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'Books'
MONGO_COLLECTION_NAME = 'Books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/id={id}'
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 3

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api(url):
    async with semaphore:
        try:
            logging.info("Scraping %s", url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.info('Error Occurred while Scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def save_date(data):
    logging.info("Saving Data %s", data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)


async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_date(data)


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, 6)]
    results = await asyncio.gather(*scrape_index_tasks)
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page) for page in range(1, PAGE_NUMBER + 1))]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info("Results %s", json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_index_tasks)
    await session.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
