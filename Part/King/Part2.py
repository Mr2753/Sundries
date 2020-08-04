# -*- coding: utf-8 -*-
# @Time     :   2020/3/28 23:59
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
