# -*- coding: utf-8 -*-
# @Time     :   2020/4/8 7:09
# @Author   :   Payne
# @File     :   4-8-Basic Test.py
# @Software :   PyCharm

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
#     await page.waitForSelector('.item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print('Names:', names)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

# async def main():
#     browser = await launch({'verify': True})
#     page = await browser.newPage()
#     await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
#     await page.waitForSelector('item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print('Names:', names)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
    browser = await launch(
        {'executablePath': executablePath,
         'headless': True, 'slowMo': 30,
         }
    )
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)


asyncio.get_event_loop().run_until_complete(main())
