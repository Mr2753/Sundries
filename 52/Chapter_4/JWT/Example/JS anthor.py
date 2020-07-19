# -*- coding: utf-8 -*-
# @Time     :   2020/5/9 9:22
# @Author   :   Payne
# @File     :   JS anthor.py
# @Software :   PyCharm
import hashlib
import time
import base64
from typing import List, Any
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
INDEX_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie?limit={limit}&offset={offset}&token={token}'
DETAIL_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie/{id}?token={token}'
LIMIT = 10
OFFSET = 0
SECRET = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'


def get_token(args: List[Any]):
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')


args = ['/api/movie']
token = get_token(args=args)
index_url = INDEX_URL.format(limit=LIMIT, offset=OFFSET, token=token)
response = requests.get(index_url)
print('response', response.json())

result = response.json()
for item in result['results']:
    id = item['id']
    print('ID:', id)
    encrypt_id = base64.b64encode((SECRET + str(id)).encode('utf-8')).decode('utf-8')
    print('encrypt_id:', encrypt_id)
    args = [f'/api/movie/{encrypt_id}']
    token = get_token(args=args)
    print('Token:', token)
    detail_url = DETAIL_URL.format(id=encrypt_id, token=token)
    print('detail_url:', detail_url)
    response = requests.get(detail_url)
    print('response', response.json())
