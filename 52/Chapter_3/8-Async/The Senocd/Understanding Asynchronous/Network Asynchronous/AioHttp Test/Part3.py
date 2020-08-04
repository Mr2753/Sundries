# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 22:29
# @Author   :   Payne
# @File     :   Part3.py
# @Software :   PyCharm
import aiohttp
import asyncio
import time

"""Timeout设置"""
# async def main():
#     timeout = aiohttp.ClientTimeout(total=3)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async with session.get('https://httpbin.org/get') as response:
#             print('Status:', response.status)
#             # print(await response.json())
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())


"""信号量设置"""
CONCURRENCY = 5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    async with semaphore:
        print('Scraping URL:', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(5)]
    await asyncio.gather(*scrape_index_tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
