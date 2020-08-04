# -*- coding: utf-8 -*-
# @Time     :   2020/4/4 0:36
# @Author   :   Payne
# @File     :   4-3-aiohttp Base.py
# @Software :   PyCharm

import aiohttp
import asyncio
import requests

'''
这里我们可以看到有些字段前面需要加await，有的则不需要。其原则是，如果其返回的是一个coroutine对象（如async修饰的方法），那么前面就要加await.
具体可以看aiohttp 的 API，其链接为：https://docs.aiohttp.org/en/stable/client_reference.html。

'''
'''基本使用'''
# 1
'''
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html:{html[:100]}...')
        print(f'status:{status}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
'''

# 2
'''Request'''
# url = 'https://httpbin.org/get'
# params = {'name': 'germey', 'age': '25'}
# response = requests.get(url, params=params)
# print(response.text)
'''Base_aiohttps'''
# async def main():
#     params = {'name': 'germey', 'age': '25'}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://httpbin.org/get', params=params) as response:
#             print(await response.text())
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())
'''aiohttps'''
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, params=params) as response:
#             print(await response.text())
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

'''超时设置'''
#
# async def main():
#     timeout = aiohttp.ClientTimeout(total=1)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async with session.get('https://httpbin.org/get') as response:
#             print('status', response.status)
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())


'''并发数量（信号量Semaphore） 控制'''
CONCURRENCY = 5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
