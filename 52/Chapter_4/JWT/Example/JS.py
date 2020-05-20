# -*- coding: utf-8 -*-
# @Time     :   2020/5/6 8:37
# @Author   :   Payne
# @File     :   JS.py
# @Software :   PyCharm

import logging
import base64
import hashlib
import time
import requests
from typing import List, Any

INDEX_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}&token={token}'
LIMIT = 10
OFFSET = 0

log = '%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s'
anthor = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO,
                    format=log)


def get_token(args: List[Any]):
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')


args = ['/api/movie']
token = get_token(args=args)
print(token)
index_url = INDEX_URL.format(limit=LIMIT, offset=OFFSET, token=token)
response = requests.get(index_url)
# print(response, '\n')
print(response.json())

# timestamp = str(int(time.time()))
# print(timestamp)
