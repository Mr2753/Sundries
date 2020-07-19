# -*- coding: utf-8 -*-
# @Time     :   2020/5/17 9:21
# @Author   :   Payne
# @File     :   demo1.py
# @Software :   PyCharm
import hashlib
import requests
import base64
import time
from typing import List, Any
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')

INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/api/movie/?limit=10&offset={offset}&token={token}'
OFFSET = 10


def getToken(agrs: List[Any]):
    # t = str(round(time.time()))
    t = str(int(time.time()))
    agrs.append(t)
    o = hashlib.sha1(','.join(agrs).encode('utf-8')).hexdigest()
    # return base64.b64encode(','.join([o, t]).encode('utf-8')).decode('utf-8')
    return base64.b64encode(str(o).encode('utf-8')).decode('utf-8')


agrs = ['/api/movie']
token = getToken(agrs)
print(token)
response = requests.get(INDEX_URL.format(offset=OFFSET, token=token))
print(response.json())
