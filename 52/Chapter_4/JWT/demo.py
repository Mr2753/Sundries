# -*- coding: utf-8 -*-
# @Time     :   2020/5/15 12:30
# @Author   :   Payne
# @File     :   demo.py
# @Software :   PyCharm
import hashlib
import io
import sys
import requests
import base64
from typing import List, Any
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
INDEX_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie/?limit=10&offset={offset}&token={token}'
OFFSET = 10


def getToken1(agrs: List[Any]) -> List:
    timestamp = str(int(time.time()))
    print('agrs:', agrs)
    agrs.append(timestamp)
    print('Another args:', agrs)
    sign = hashlib.sha1(','.join(agrs).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')


agrs = ['/api/movie']
token = getToken1(agrs)
# print(token)
response = requests.get(INDEX_URL.format(offset=OFFSET, token=token))
print(response.json())
