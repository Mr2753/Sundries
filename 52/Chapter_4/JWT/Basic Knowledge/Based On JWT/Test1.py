# -*- coding: utf-8 -*-
# @Time     :   2020/4/28 12:31
# @Author   :   Payne
# @File     :   Test1.py
# @Software :   PyCharm
import io
import sys
from urllib.parse import urljoin
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
"""
模拟登录思路：
模拟登录结果，带上必要的登录信息，获取JWT
后续的登录子啊Request Headers里面加上Authorization 字段，值就是JWT对应的内容
"""

Base_URL = 'https://login3.scrape.cuiqingcai.com/'
LOGIN_URL = urljoin(Base_URL, '/api/login')
INDEX_URL = urljoin(Base_URL, '/api/book')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, json={
    'username': USERNAME,
    'password': PASSWORD
})
data = response_login.json()
print('Response JSON:', data)
jwt = data.get('token')
print('JWT', jwt)
header = {
    'Authorization': f'jwt {jwt}'
}
response_index = requests.get(INDEX_URL, params={
    'limit': 18,
    'offset': 0
}, headers=header)
print('Response Status:', response_index.status_code)
print('Response URL:', response_index.url)
print('Response Data:', response_index.json())
# print('Response results:', response_index.json()['results'])
for result in response_index.json()['results']:
    id = result['id']
    name = result['name']
    cover = result['cover']
    score = result['score']
    authors = result['authors']
    for author in authors:
        print(author)
    print(id, name, cover, score)
