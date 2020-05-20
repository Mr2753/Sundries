# -*- coding: utf-8 -*-
# @Time     :   2020/5/15 8:34
# @Author   :   Payne
# @File     :   Js Detail.py
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


#
def get_token(args: List[Any]):
    timestamp = str(int(time.time()))
    logging.info('timestamp: %s' % timestamp)
    args.append(timestamp)
    logging.info('args: %s' % args)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    logging.info('sign: %s' % sign)
    result = base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')
    logging.info('result: %s' % result)
    return result


args = ['/api/movie']
token = get_token(args=args)
# index_url = INDEX_URL.format(limit=LIMIT, offset=OFFSET, token=token)
# response = requests.get(index_url)
# # print(response, '\n')
# print(response.json())

# timestamp = str(int(time.time()))
# print(timestamp)
time = str(int(time.time()))
one = ['/api/movie', time]
a = ','.join(one)
A = ','.join(one).encode('utf-8')
print(a)
print(A)
two = hashlib.sha1(A).hexdigest()
print(two)
