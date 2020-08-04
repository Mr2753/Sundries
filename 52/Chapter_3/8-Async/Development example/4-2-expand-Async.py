# -*- coding: utf-8 -*-
# @Time     :   2020/4/2 21:05
# @Author   :   Payne
# @File     :   4-2-expand-Async.py
# @Software :   PyCharm

import aiohttp
import time
import asyncio


def test(number):
    start_time = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.time()
    print('Number:', number, 'Cost Time:', end_time - start_time)


for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)
