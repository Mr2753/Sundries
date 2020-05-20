# -*- coding: utf-8 -*-
# @Time     :   2020/5/6 10:00
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm
import asyncio
from pyppeteer import launch

width, height = 1366, 768

BASE_URL = 'https://dynamic2.scrape.cuiqingcai.com/'


async def main():
    executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
    browser = await launch(
        {'executablePath': executablePath,
         'headless': False, 'slowMo': 30,
         }
    )
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto(BASE_URL)
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot(path='example.png')
    dimensions = await page.evaluate('''() => {
        return {
        width:document.documentElement.clientWidth,
        height:document.documentElement.clientHeight,
        deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
