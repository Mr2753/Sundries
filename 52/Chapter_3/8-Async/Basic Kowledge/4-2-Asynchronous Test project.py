# -*- coding: utf-8 -*-
# @Time     :   2020/4/3 11:56
# @Author   :   Payne
# @File     :   4-2-Asynchronous Test project.py
# @Software :   PyCharm

import asyncio
import time
import aiohttp

# start_time = time.time()
#
#
# async def get(url):
#     session = aiohttp.ClientSession()
#     response = await session.get(url)
#     await response.text()
#     await session.close()
#     return response

#
# async def request():
#     # url1 = 'https://static4,scrape.cuiqingcai.com/'
#     url = 'https://static4.scrape.cuiqingcai.com/'
#     print('Waiting for', url)
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             # response = await get(url)
#             print('Get response from', url, 'response', response)
#
#
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end_time = time.time()
# print('Cost time', end_time - start_time)
''''''

# async def test(number):
#     start_time = time.time()
#     # async def get(url):
#     #     session = aiohttp.ClientSession()
#     #     response = await session.get(url)
#     #     await response.text()
#     #     await session.close()
#     #     return response
#     #
#     # async def request():
#     #     url = 'https://www.baidu.com/'
#     #     await get(url)
#     url = 'https://static4.scrape.cuiqingcai.com/'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             print('Get response from', url, 'response', response)
#
#     tasks = [asyncio.ensure_future(request()) for _ in range(number)]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     end_time = time.time()
#     print('Number:', number, 'Cost Time:', end_time - start_time)
#
#
# for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200, 500]:
#     test(number)

url = 'https://www.baidu.com/'


async def test(number):
    start_time = time.time()
    # async def get(url):
    #     session = aiohttp.ClientSession()
    #     response = await session.get(url)
    #     await response.text()
    #     await session.close()
    #     return response
    async with aiohttp.ClientSession() as session:
        # async def request():
        #     url = 'https://www.baidu.com/'
        #     await get(url)
        #     await request()

        # tasks = [asyncio.ensure_future(request()) for _ in range(number)]
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(asyncio.wait(tasks))
        async with session.get(url) as response:
            print('Get response from', url, 'response', response)
    end_time = time.time()
    print('Number:', number, 'Cost Time:', end_time - start_time)


# for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200, 500]:
# test(number)
tasks = [asyncio.ensure_future(test(number)) for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200, 500]]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
