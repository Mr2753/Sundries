# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 18:59
# @Author   :   Payne
# @File     :   Part2.py
# @Software :   PyCharm

import asyncio
import requests
import time

BASE_URL = 'https://static4.scrape.cuiqingcai.com/'
Start = time.time()

"""常错示例"""

'''Test 1 （伪异步）'''
# await 的用法
# 使用await可以将耗时等待的操作（过程）挂起，让出控制权， 转而去执行下一个任务

"""
async def request():
    print('Wait for %s ...' % BASE_URL)
    response = requests.get(BASE_URL)
    print('Get Response From:', BASE_URL, 'Response:', response)


# 将函数注入到任务（Tasks）
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# 调用函数
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
End = time.time()
print("GET TIME:", End - Start)"""

'''Test 2'''
# TypeError: object Response can't be used in 'await' expression
# 错误原因：await 方法所输出的类型与asyncio.wait方法不符合
# 根据官方文档得知：
# await 后面对象必须是以下格式之一：
# 一个原生的coroutine对象: A native coroutine object returned from a native coroutine function.
# 一个由 types.coroutine 修饰的生成器，这个生成器可以返回 coroutine 对象:A generator-based coroutine object returned from a function
# decorated with types.coroutine().
# 一个包含 __await__ 方法的对象返回的一个迭代器:An object with an __await__ method returning an iterator.An object with an __await__
# method returning an iterator


"""
async def request():
    print("Wait For %s ..." % BASE_URL)
    response = await requests.get(BASE_URL)
    print("GET Response From", BASE_URL, 'Response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
"""
