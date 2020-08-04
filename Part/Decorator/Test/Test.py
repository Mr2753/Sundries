# -*- coding: utf-8 -*-
# @Time     :   2020/5/1 1:36
# @Author   :   Payne
# @File     :   Test.py
# @Software :   PyCharm
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


def func(url):
    def scrape(*args, **kwargs):
        try:
            response = requests.get(url())
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"The Response Status {response.status_code}", response.text)
        except Exception as e:
            print(e)
        return url(*args, **kwargs)

    return scrape


@func
def scrape_index():
    return 'https://www.baidu.com'


print(scrape_index())
