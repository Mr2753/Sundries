# -*- coding: utf-8 -*-
# @Time     :   2020/4/2 19:19
# @Author   :   Payne
# @File     :   Base Async.py
# @Software :   PyCharm

import asyncio
import io
import sys

import requests

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
'''
async def execute(x):
    print('Number:coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("After calling loop")
'''

# 通过asyncio 中ensure_future 返回test对象
'''
async def execute(x):
    print('Number:', x)
    return x


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
task = asyncio.ensure_future(coroutine)
print('Task', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task', task)
print("After calling loop")
'''

# 绑定回调 为某个task 绑定一个回调方法
'''
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Status', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
'''

# 直接在task 运行完毕后调用 result 方法
'''
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

coroutine = request()
task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task：', task)
print('Task Result:', task.result())
'''

'''基本多任务协程'''


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(1, 5)]
print('Task', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
