# -*- coding: utf-8 -*-
# @Time     :   2020/5/1 9:47
# @Author   :   Payne
# @File     :   Test-2.py
# @Software :   PyCharm

import requests


# def makehtml(url):
#     def wrappend():
#         # return 'html' + fn() + 'html'
#         return requests.get(url())
#
#     return wrappend
#
#
# @makehtml
# def test1():
#     return 'https://www.baidu.com'
#
#
# print(test1())


def scrape(url):
    print('Scraping URL:', url())

    def get():
        try:
            response = requests.get(url())
            if response.status_code == 200:
                print('The Response Status:', response.status_code)
            else:
                print("Response.status_code <> 200:", response.status_code)
        except Exception as e:
            print('Exception:', e)
    return get


# @scrape('https://www.baidu.com')
# def scrape_index():
#     return 'https://www.baidu.com'


# print(scrape_index())
