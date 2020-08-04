# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 20:25
# @Author   :   Payne
# @File     :   Part3-1.py
# @Software :   PyCharm

import asyncio
import aiohttp
import time


def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://cuiqingcai.com/9160.html'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print("Number:", number, 'Cost Time', end - start)


for number in [1, 3, 5, 7, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)

