# -*- coding: utf-8 -*-
# @Time     :   2020/4/29 21:09
# @Author   :   Payne
# @File     :   Part2.py
# @Software :   PyCharm

"""
一、with as 语句 前面同样需要加async 来修饰
在Python中 with... as..。 语句用于声明一个上下文管理器，能够自动的分配资源和释放资源
在异步方法中，with...as.. 前面加上async代码声明一个支持异步的上下文管理器

二、对于一些返回coroutine的操作，前面需要加await来修饰
如response 调用text方法
查询API可以发现是Coroutine 对象，，那么前面就需要加await
对于状态码来说，就不需要await
"""
import aiohttp
import asyncio
import time

'''
session.post('http://httpbin.org/post', data=b'data')
session.put('http://httpbin.org/put', data=b'data')
session.delete('http://httpbin.org/delete')
session.head('http://httpbin.org/get')
session.options('http://httpbin.org/get')
session.patch('http://httpbin.org/patch', data=b'data')
'''

# Get请求
'''
async def main():
    params = {'name': 'Payne', 'age': '20'}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
'''

# Post请求
'''
async def main():
    data = {'name': 'Payne', 'age': '20'}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
'''

'''Test'''
'''
async def main():
    data = {'name': 'Payne', 'age': 20}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print('Status:', response.status)
            print('Headers:', response.headers)
            print('Body:', await response.text())
            print('Bytes:', await response.read())
            print('Json:', await response.json())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
'''



