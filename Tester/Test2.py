# -*- coding: utf-8 -*-
# @Time     :   2020/5/13 17:56
# @Author   :   Payne
# @File     :   Test2.py
# @Software :   PyCharm
import requests
from pyquery import PyQuery as pq
import io
import sys
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1841818102.1589348170; _gid=GA1.2.692141637.1589348170; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1589348168,1589361182; footprints=eyJpdiI6IjdZb3VVK2w4eHR0V3BPUXpickRpd3c9PSIsInZhbHVlIjoiaDJ5NjdHZkNaaTJYMkx0NGtUUXdPWE9tczA4MUdkem9jQ0RJNkxtejJDUmNkamVrWHVxY1RuU2ZYVmxMM3RxcSIsIm1hYyI6IjIxZDcxM2VkNDkxOWUyZTUxYWRhYTAyM2RlYmVjZmM1OTIwN2JkYjZmNjA0ZDAwODY3NDNhNGIxNjQ1MzJkNmMifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImVSZFJLaVN4U0xsMThxekRyc1kzNEE9PSIsInZhbHVlIjoiYjFZZlZxMCtJb0ZrOGVneldUaUp2TG44UHFrNU40REc4bm1qMWJ1M1dOYXoxMktqZmMxUStmVXZ0OWYwWFFFdiIsIm1hYyI6IjM1YmQ2YWVlZDFhYjA0MzZmMDE4YjFlNmI5ZGMyYzhiMmYzYjE0ODgxNmMyZDU1YzkxMjNkNjJhMmNhYjYxZDYifQ%3D%3D; glidedsky_session=eyJpdiI6ImJ6ZkVOTmRkZW5aaWI4UmRZbFc4M0E9PSIsInZhbHVlIjoiZVd6eUZPRWs0bXp4M203andkZDQ3YWNQNEt4WUt0aUhaQk4wWXZvV3A0TFRBdWtObmxCdzBlbDFrTk9oWUt3ViIsIm1hYyI6ImE1OTI2YzFmOTM2NDdjNjJiYzg5Y2E0OGYzMWVkM2E1YmE3Yjc3NjExOWRhMTkwMGE3NWY4YWMyMGU2ZmJjYTEifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1589362063',
    'DNT': '1',
    'Host': 'www.glidedsky.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.glidedsky.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',

}
for page in range(1, 1001):
    url = f'http://www.glidedsky.com/level/web/crawler-basic-2?page={page}'
    response = requests.get(url, headers=header)
    time.sleep(3)
    print(response)
    # doc = pq(response.text)
    # data = doc('#app > main > div.container > div > div > div').text()
    # print(data)
