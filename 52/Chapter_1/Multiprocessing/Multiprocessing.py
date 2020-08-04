#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import multiprocessing
# import time

# 基本多进程
'''
def process(index):
    print(f'Process:{index}')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()
'''

# CPU显示
'''
def process(index):
    time.sleep(index)
    print(f'Process:{index}')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()
    print(f'CPU number:{multiprocessing.cpu_count()}')
    for p in multiprocessing.active_children():
        print(f'Child process name: {p.name} id:{p.pid}')
    print('Process Ended')
'''

# 守护进程 p.daemon =True
'''
from multiprocessing import Process
import time

class My_Process(Process):
    def __init__(self,loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
        print(f'Pid:{self.pid} LoopCount:{self.count}')

if __name__ == '__main__':
    for i in range(2,5):
        p = My_Process(i)
        p.daemon =True
        p.start()
    print('Main Process Ended')
    
'''

# 线程阻塞 p.join
'''
from multiprocessing import Process
import time

class My_Process(Process):
    def __init__(self,loop):
        Process.__init__(self)
        self.loop = loop
        def run(self):
            for count in range(self.loop):
                time.sleep(1)
            print(f'Pid:{self.pid} LoopCount:{self.count}')

if __name__ == '__main__':
    processes = []
    for i in range(2, 5):
        p = My_Process(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join(1)
        print(processes)
    print('Main Process Ended')
    '''

# 互斥锁
'''
from multiprocessing import Process,Lock
import time

class My_Process(Process):
    def __init__(self,loop,lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            self.lock.acquire()
            print(f'Pid:{self.pid} LoopCount:{count}')
            self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10,15):
        p = My_Process(i, lock)
        p.start()
'''

# 信号量 Semaphore
'''
# from multiprocessing import Process,Semaphore,Lock,Queue
# import time
# 
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
# 
# class Consumer(Process):
#     def run(self):
#         global buffer,empty,full,lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             buffer.get()
#             print('Consumer pop an element')
#             time.sleep(1)
#             lock.release()
#             empty.release()
# 
# class Producer(Process):
#     def run(self):
#         global buffer,empty,full,lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             buffer.put(1)
#             print('Producer append an element')
#             time.sleep(1)
#             lock.release()
#             full.release()
# 
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon =True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('Main Process Ended')
# 
'''

# 信号量、队列
'''
from multiprocessing import Process,Semaphore,Lock,Queue
import time
from random import random

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()

class Consumer(Process):
    def run(self):
        global buffer,empty,full,lock
        while True:
            full.acquire()
            lock.acquire()
            print(f'Consumer get {buffer.get()}')
            time.sleep(1)
            lock.release()
            empty.release()
    
class Producer(Process):
    def run(self):
        global buffer,empty,full,lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            print(f'Producer put {num}')
            buffer.put(num)
            time.sleep(1)
            lock.release()
            full.release()

if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Enden')
    '''

# 管道 默认声明 Pipe 对象是双向管道，如果要创建单向管道，可以在初始化的时候传入 deplex 参数为 False

'''
from multiprocessing import Process,Pipe

class Consumer(Process):
    def __init__(self,pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send('Consumer Words')
        print(f'Consumer Received: {self.pipe.recv()}')

class Producer(Process):
    def __init__(self,pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print(f'Producer Receiverd: {self.pipe.recv()}')
        self.pipe.send('Producer words')

if __name__ == '__main__':
    pipe = Pipe()
    p = Producer(pipe[0])
    c = Consumer(pipe[1])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
    '''

from multiprocessing import Pool
import urllib.request
import urllib.error


def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'URL {url} Scraped')
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f'URL {url} not Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = ['https://www.baidu.com',
            'http://www.meituan.com/',
            'http://blog.csdn.net/',
            'http://xxxyxxx.net',
            ]
    pool.map(scrape, urls)
    pool.close()
