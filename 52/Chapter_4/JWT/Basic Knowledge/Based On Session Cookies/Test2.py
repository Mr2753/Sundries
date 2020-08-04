# -*- coding: utf-8 -*-
# @Time     :   2020/4/28 13:40
# @Author   :   Payne
# @File     :   Test2.py
# @Software :   PyCharm
import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.cuiqingcai.com/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'
# allow_redirects=False 禁用requests方法的自动重定向
response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False)

cookies = response_login.cookies
print("Response_Login Cookies:", cookies)

response_index = requests.get(INDEX_URL, cookies=cookies)
print("Response Status:", response_index.status_code)
print('Response URL:', response_index.url)
# print('Response Text:\n', response_index.text)

'''会话维持'''
# with requests.Session() as session:
#     session.post(LOGIN_URL, data={
#         'username': USERNAME,
#         'password': PASSWORD
#     }, allow_redirects=False)
#     cookies = session.cookies
#     print("This with Cookies", cookies)
