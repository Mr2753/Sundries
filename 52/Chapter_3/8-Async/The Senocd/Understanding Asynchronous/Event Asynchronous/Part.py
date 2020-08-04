# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 17:16
# @Author   :   Payne
# @File     :   Part.py
# @Software :   PyCharm

import asyncio


async def execute(x):
    print('Number:', x)


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After Calling Execute')


loop = asyncio.get_event_loop().run_until_complete(coroutine)
print()