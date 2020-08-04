#!/usr/bin/python3
# -*- coding: utf-8 -*-
import io
import sys
import parsel
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response = requests.get('https://www.baidu.com',headers=header)
response.encoding = response.apparent_encoding
# print(response.text)
sel = parsel.Selector(response.text)
one = sel.css('.s_tab_inner a ::attr(href)').get()
print(one)
