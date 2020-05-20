# -*- coding: utf-8 -*-
# @Time     :   2020/5/9 15:21
# @Author   :   Payne
# @File     :   Test.py
# @Software :   PyCharm
import base64

for id in range(1, 11):
    SECRET = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
    encrypt_id = base64.b64encode((SECRET + str(id)).encode('utf-8')).decode('utf-8')
    print(encrypt_id)
