# -*- coding: utf-8 -*-
# @Time     :   2020/5/3 0:38
# @Author   :   Payne
# @File     :   Another.py
# @Software :   PyCharm
import requests

URL = 'https://www.lagou.com/'
print(requests.get(URL).text)