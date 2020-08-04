#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import time

'''
count = 0

class My_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count
        temp = count + 1
        time.sleep(1)
        count = temp



threads = []
for _ in range(10):
    thread = My_Thread()
    thread.start()
    threads.append(thread)
    for thread in threads:
        thread.join()
        print(f'Final count:{count}')
print(threads)
'''

'''
count = 0
class My_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()
        temp = count + 1
        time.sleep(1)
        count = temp
        lock.acquire()


lock = threading.Lock()
threads = []
for _  in range(10):
    thread = My_Thread()
    thread.start()
    threads.append(thread)
    for thread in threads:
        thread.join()
        print(f'Final count:{count}')
'''
