# -*- coding: utf-8 -*-
# @Time     :   2020/4/20 9:07
# @Author   :   Payne
# @File     :   AioHttp_Base.py
# @Software :   PyCharm

import aiohttp
import asyncio
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

Base_URL = 'https://www.4399.com'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, Base_URL)
        print(f'Html:{html}...')
        print(f'Status:{status}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop().run_until_complete(main())
