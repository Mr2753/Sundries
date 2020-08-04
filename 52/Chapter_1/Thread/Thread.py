# -*- coding: utf-8 -*-
# @Time     :   2020/3/31 17:22
# @Author   :   Payne
# @File     :   Thread.py
# @Software :   PyCharm

import threading
import time

'''基本实现'''

'''
def target(second):
    print(f'Threading {threading.current_thread().name} is Running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is Running')
for i in [1, 5]:
    thread = threading.Thread(target=target, args=[i])
    thread.start()
# print(f'Threading {threading.current_thread().name} is ended')

'''

