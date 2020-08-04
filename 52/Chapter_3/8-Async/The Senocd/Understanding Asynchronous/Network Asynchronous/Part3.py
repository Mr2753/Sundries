# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 20:10
# @Author   :   Payne
# @File     :   Part3.py
# @Software :   PyCharm

import asyncio
import aiohttp
import time

Start = time.time()

BASE_URL = 'https://static4.scrape.cuiqingcai.com/'


async def get():
    session = aiohttp.ClientSession()
    response = await session.get(BASE_URL)
    await response.text()
    await session.close()
    return response


async def request():
    print('Wait For', BASE_URL)
    response = await get()
    print('Get Response From:', BASE_URL, '\n', ' Response:', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
End = time.time()
print('Cost Time :', End - Start)
