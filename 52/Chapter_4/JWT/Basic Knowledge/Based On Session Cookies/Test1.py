# -*- coding: utf-8 -*-
# @Time     :   2020/4/28 12:31
# @Author   :   Payne
# @File     :   Test1.py
# @Software :   PyCharm
import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.cuiqingcai.com/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False)
# 获取cookies
response_index = requests.get(INDEX_URL)
# print('Response_Index.Status:', response_index.status_code)
# print('Response_URL :', response_index.url)
# print('Response Text :', response_index.text)
cookies = response_login.cookies
print("Cookies:", cookies)
