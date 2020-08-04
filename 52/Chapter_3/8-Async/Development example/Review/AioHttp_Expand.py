# -*- coding: utf-8 -*-
# @Time     :   2020/4/20 9:43
# @Author   :   Payne
# @File     :   AioHttp_Expand.py
# @Software :   PyCharm

import aiohttp
import asyncio

'''Basic Use'''
# Basic Requests
'''
async def main():
    params = {'name': 'Payne', 'Age': "20"}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

'''

# Timeout Setting
'''
async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://httpbin.org/get') as response:
            print("status:", response.status)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
'''

# semaphore Setting
'''
CONCURRENCY = 5
URL = 'https://www.baidu.com'

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    async with semaphore:
        print('Scraping:', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(3)]
    await asyncio.gather(*scrape_index_tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

'''