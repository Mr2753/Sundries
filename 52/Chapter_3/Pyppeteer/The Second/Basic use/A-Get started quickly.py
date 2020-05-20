# -*- coding: utf-8 -*-
# @Time     :   2020/5/6 9:37
# @Author   :   Payne
# @File     :   A-Get started quickly.py
# @Software :   PyCharm

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

BASE_URL = 'https://dynamic2.scrape.cuiqingcai.com/'
executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'


async def main():
    browser = await launch(
        {'executablePath': executablePath,
         'headless': False}
    )
    page = await browser.newPage()
    await page.goto(BASE_URL)
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await browser.close()


asyncio.run(main())
