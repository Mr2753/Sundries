# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 20:42
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm

import asyncio
import io
import sys

import aiohttp
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'Status:{status}')
        print(f'Html: {html}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
