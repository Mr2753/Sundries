# -*- coding: utf-8 -*-
# @Time     :   2020/4/11 9:28
# @Author   :   Payne
# @File     :   411-Pyppeteer.py
# @Software :   PyCharm

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

url = 'https://dynamic2.scrape.cuiqingcai.com/'

'''基本使用'''
# '''
# async def main():
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': True,
#          'slowMo': 30,
#          }
#     )
#     page = await browser.newPage()
#     await page.goto(url)
#     await page.waitForSelector('.item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print("Name:", names)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())
# '''

# 配置使用


''''''
width, height = 1366, 768

# async def main():
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': False, 'slowMo': 30,
#          }
#     )
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto(url)
#     await page.waitForSelector('.item .name')
#     await asyncio.sleep(2)
#     await page.screenshot(path='example.png')
#     dimensions = await page.evaluate('''() => {
#         return {
#         width:document.documentElement.clientWidth,
#         height:document.documentElement.clientHeight,
#         deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#
#     print(dimensions)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''无头模式'''
# async def main():
#     # await launch(header=False,)
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': False, 'slowMo': 30,
#          }
#     )
#     await asyncio.sleep(100)
# asyncio.get_event_loop().run_until_complete(main())


'''调试模式'''

#
# async def main():
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': False,
#          'slowMo': 30,
#          'devtools': True
#          }
#     )
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())


'''禁用提示条False'''
# async def main():
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': False,
#          'slowMo': 30,
#          # 'devtools': True
#          'args': ['--disable-infobars']
#          }
#
#     )
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''防止检测'''
#
# async def main():
#     # browser = await launch()
#     executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
#     browser = await launch(
#         {'executablePath': executablePath,
#          'headless': False,
#          'slowMo': 30,
#          'args': ['--disable-infobars'],
#          }
#     )
#     page = await browser.newPage()
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
#     await page.goto('https://antispider1.scrape.cuiqingcai.com/')
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''选项卡操作'''


async def main():
    executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
    browser = await launch(
        {'executablePath': executablePath,
         'headless': False, 'slowMo': 30,
         }
    )
    page = await browser.newPage()
    await page.goto(url)
    page = await browser.newPage()
    await page.goto('https://www.bing.com')
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    pages = await browser.pages()
    print('Pages:', pages)
    page1 = pages[1]
    await page1.bringToFront()
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
