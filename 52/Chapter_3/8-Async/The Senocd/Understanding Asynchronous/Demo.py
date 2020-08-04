# -*- coding: utf-8 -*-
# @Time     :   2020/4/30 0:44
# @Author   :   Payne
# @File     :   Demo.py
# @Software :   PyCharm
import json
import aiohttp
import asyncio
import time
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

CONCURRENCY = 5
# URL = 'https://www.baidu.com'
URL = 'https://cuiqingcai.com/9160.html'
semaphore = asyncio.Semaphore(CONCURRENCY)


# session = None


async def scrape_api():
    async with semaphore:
        print('Scraping', URL)
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                await asyncio.sleep(1)
                return await response.text()


async def main():
    # global session
    # session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(100)]
    results = await asyncio.gather(*scrape_index_tasks)
    print('Results %s', json.dumps(results, ensure_ascii=False, indent=2))
    # for result in results:
    #     print(result)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
