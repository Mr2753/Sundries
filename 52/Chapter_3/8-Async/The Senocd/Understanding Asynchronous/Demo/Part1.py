# -*- coding: utf-8 -*-
# @Time     :   2020/5/6 21:16
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm

import aiohttp
import asyncio
import logging
import re
from bs4 import BeautifulSoup

# BASE_URL = 'https://www.guazi.com/cs/buy/o' + str(i) + '/#bread'
CONCURRENCY = 5
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

loop = asyncio.get_event_loop()


class Car(object):

    def __init__(self):
        self.semaphore = asyncio.Semaphore(CONCURRENCY)
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'rfnl=https://www.guazi.com/cs/buy/o; antipas=097768008M9b333b98852413M7',
            'DNT': '1',
            'Host': 'www.guazi.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.guazi.com/cs/buy/o',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        }

    async def Scrape(self, url):
        """
        @param: all url
        @return: response
        """
        async with self.semaphore:
            try:
                async with aiohttp.ClientSession(headers=self.header).get(url) as response:
                    if response.status == 200:
                        # logging.info(await response.text())
                        return response
                    else:
                        logging.debug("The Status <> 200", response)
            except aiohttp.ClientError:
                logging.error('AioHttp.ClientError', aiohttp.ClientError)
            except aiohttp.ClientTimeout:
                logging.error('AioHttp.ClientTimeout', aiohttp.ClientTimeout)

    async def scrape_index(self, page):
        url = 'https://www.guazi.com/cs/buy/o' + str(page) + '/#bread'
        html = await self.Scrape(url)
        await self.parse_index(html)

    async def parse_index(self, html):
        # 解析
        soup = BeautifulSoup(html, 'html.parser')
        infos = soup.find('ul', {"class": "carlist clearfix js-top xh-highlight"}).find('li')
        print(infos)
        with open(r'guazi.csv', 'a+', encoding='utf-8') as f:
            for info in infos:
                # 类型
                leixing = info.find('h2').get_text()
                print(leixing)
                # 年份
                nianfen1 = info.find('div', {'class': 't-i'}).get_text()
                # print(nianfen1)
                nianfen2 = re.sub(r'|', '', nianfen1).split('|')
                # print(nianfen2)
                nianfen = nianfen2[0]
                print(nianfen)
                # 里程
                licheng1 = re.sub(r'|', '', nianfen1).split('|')[1]
                print(licheng1)
                # 服务类型
                fuwu = re.sub(r'|', '', nianfen1).split('|')[2]
                print(fuwu)

                # 地点
                didian = '长沙'
                # 售价
                shoujia = info.find('div', {'class': 't-price'}).get_text()
                print(shoujia)
                # 原价
                try:
                    yuanjia = info.find('div', {'class': 't-price'}).get_text()
                except AttributeError:
                    yuanjia = ''
                return yuanjia

    async def main(self):
        scrape_tasks = [asyncio.ensure_future(self.scrape_index(page)) for page in range(2)]
        await asyncio.gather(*scrape_tasks)


if __name__ == '__main__':
    car = Car()
    loop.run_until_complete(car.main())
