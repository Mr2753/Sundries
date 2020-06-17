#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

url = 'https://static1.scrape.cuiqingcai.com/'
url1 = 'http://httpbin.org/get'
url2 = 'http://www.baidu.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
# 182.33.248.131
# 122.4.215.33

import requests

'''
r = requests.get(url1)
print(r)
print(r.text)
'''

#
# r = requests.get(url)
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern,r.text)

'''
# r.status_code   请求的状态码
# r.headers           得到请求的头
# r.cookies       得到请求的cookies
# r.history         得到请求的历史
'''

'''
r = requests.get(url)
exit( ) if not r.status_code == requests.codes.ok else print('Succesfully')
'''

# cookies解析
'''
r = requests.get('http://www.baidu.com')
print(r.cookies)
print(r.cookies.items())
for key,value in r.cookies.items():
    print(key + '=' + value)
    '''

'''Session维持'''
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/nymber/123456')
# r = s.get('http://httpbin.org/cookies')
# print(s.text)
# print(res)
# r = requests.session(url=url2, headers=header)
# print(r)
# # print(r)

# session = requests.get('https://www.baidu.com/',headers=header)
# cookies = session.headers
# print(cookies)

# s = requests.Session()
#
# r = requests.get('http://www.baidu.com',headers=header)
# # print(r)
# # print('*'*80)
# # print('网页源码',r.text)
# # print('*'*80)
# # print('response cookies',r.cookies)
# # print('*'*80)
# print('response headers',r.headers)
# # print('*'*80)

'''获取cookies'''
s = requests.Session()
s.get('http://www.baidu.com', headers=header)
r = s.get('http://www.baidu.com', headers=header)
print(r.request.headers['cookie'])

with requests.Session() as s:
    s.get('http://www.baidu.com', headers=header)
    r = s.get('http://www.baidu.com', headers=header)
    print(r.request.headers['Cookie'])

'''
{'Bdpagetype': '1', 'Bdqid': '0x8d7e219700056582', 'Cache-Control': 'private', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html;charset=utf-8', 'Date': 'Thu, 12 Mar 2020 03:47:36 GMT', 'Expires': 'Thu, 12 Mar 2020 03:47:25 GMT', 'Server': 'BWS/1.1', 'Set-Cookie': 'BDSVRTM=1; path=/, BD_HOME=1; path=/, H_PS_PSSID=30963_1420_21113_30997_31055_30824_30717; path=/; domain=.baidu.com', 'Strict-Transport-Security': 'max-age=172800', 'Traceid': '1583984856027220020210195623538837513602', 'X-Ua-Compatible': 'IE=Edge,chrome=1', 'Transfer-Encoding': 'chunked'}
{'Bdpagetype': '1', 'Bdqid': '0x8d7e219700056582', 'Cache-Control': 'private', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html;charset=utf-8', 'Date': 'Thu, 12 Mar 2020 03:47:36 GMT', 'Expires': 'Thu, 12 Mar 2020 03:47:25 GMT', 'Server': 'BWS/1.1', 'Set-Cookie': 'BDSVRTM=1; path=/, BD_HOME=1; path=/, H_PS_PSSID=30963_1420_21113_30997_31055_30824_30717; path=/; domain=.baidu.com', 'Strict-Transport-Security': 'max-age=172800', 'Traceid': '1583984856027220020210195623538837513602', 'X-Ua-Compatible': 'IE=Edge,chrome=1', 'Transfer-Encoding': 'chunked'}

'''

# '''SSL验证'''
# '''
# from requests.packages import urllib3
# import logging
# url2 = 'https://static2.scrape.cuiqingcai.com/'
# # '''忽略警告''' # urllib3.disable_warnings()
# # '''捕获警告到日志方式忽略警告''' # logging.captureWarnings(True)
# #
# # response = requests.get(url2,verify=False)
# # print(response)
# # '''

'''身份认证'''
# from  requests.auth import HTTPBasicAuth
#
# url3 = 'https://static3.scrape.cuiqingcai.com/'
# # r = requests.get(url3,auth=HTTPBasicAuth('admin','admin'))
# r = requests.get(url3,auth=('admin','admin'))
# print(r)
'' \
    # url4 = 'https://api.github.com/events'
# proxies = {
#
# }


# s = requests.Session()
# s.get('https://www.baidu.com/')
# r = s.get('https://www.baidu.com/')
# print(r)
