# -*- coding: utf-8 -*-
# @Time     :   2020/4/12 14:35
# @Author   :   Payne
# @File     :   412-Async.py
# @Software :   PyCharm
import asyncio

import requests
import logging
import time
import aiohttp
import asyncio

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
TOTAL_NUMBER = 5
BASE_URL = 'https://static4.scrape.cuiqingcai.com/'
'''单线程'''
# start = time.time()
# for id in range(1, TOTAL_NUMBER + 1):
#     url = BASE_URL.format(id=id)
#     logging.info('Scraping %s', url)
#     response = requests.get(url)
# end = time.time()
# logging.info('Total Time %s Seconds', end - start)

'''基本协程'''

# async def execute(x):
#     print('Number:', x)
#
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
#
# loop = asyncio.get_event_loop().run_until_complete(coroutine)
# print('After calling loop')


'''多任务协程'''


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks：', tasks)

loop = asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task Result:", task.result())

'''AioHttp基本使用'''
start = time.time()

# async def get(BASE_URL):
#     session = aiohttp.ClientSession()
#     response = await session.get(BASE_URL)
#     await response.text()
#     await session.close()
#     return response
#
#
# async def request(number):
#     # url = 'https://www.baidu.com'
#     print("Waiting For:", BASE_URL)
#     response = await get(BASE_URL)
#     print('Get Response From', BASE_URL, "Response:", response)
#     print('Number:', number)


# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# tasks = [asyncio.ensure_future(request(number)) for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200]]
# loop = asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
# aiohttp.ClientSession()
# end = time.time()
# print('Cost Time:', end - start)


'''AioHttp'''

# async def get(number):
#     start = time.time()
#     try:
#         logging.info('Scraping %s', BASE_URL)
#         async with aiohttp.ClientSession() as session:
#             async with session.get(BASE_URL) as response:
#                 print('Get response from', BASE_URL, 'response', response)
#         end = time.time()
#         print('Number:', number, 'Cost Time:', end - start)
#                 # return await response.text()
#
#     except aiohttp.ClientError as error:
#         logging.info("AioHttp.ClientError:", error)
#
#
# async def scrape(number):
#     return await get(number)
#
#
# tasks = [asyncio.ensure_future(get(number)) for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200]]
# loop = asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
