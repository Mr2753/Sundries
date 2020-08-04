# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 18:34
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm

import asyncio
import requests

"""单次请求"""

#
# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status
#
#
# def callback(task):
#     print('Status:', task.result())
#
#
# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print("Task:", task)
#
# loop = asyncio.get_event_loop().run_until_complete(task)
# print("Task:", task)

"""
多次请求
首先定义一个列表，然后使用asyncio.await方法即可执行
"""


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(100)]
# print("Tasks:", tasks)
loop = asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task:', task)
    print("Task Result:", task.result())
