# -*- coding: utf-8 -*-
# @Time     :   2020/4/2 19:54
# @Author   :   Payne
# @File     :   4-2-Achieve Async.py
# @Software :   PyCharm


import asyncio
# import requests
import time
import aiohttp

# 伪异步 not hung
'''
async def request():
    url = 'https://static4.scrape.cuiqingcai.com'
    print('Wait for', url)
    # response = await requests.get(url)
    response = requests.get(url)
    print('Get response from', url, 'response', response)


Start_time = time.time()
tasks = [asyncio.ensure_future(request()) for _ in range(2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

End_time = time.time()
print("Cost time", End_time - Start_time)
'''

start_time = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    # url1 = 'https://static4,scrape.cuiqingcai.com/'
    url = 'https://static4.scrape.cuiqingcai.com/'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
print('Cost time', end_time - start_time)
