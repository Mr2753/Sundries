# -*- coding: utf-8 -*-
# @Time     :   2020/5/1 23:03
# @Author   :   Payne
# @File     :   Demo1.py
# @Software :   PyCharm


"""装饰器(函数)"""

"""
函数编程：
一、定义函数：将函数装到里面
二、函数名（）：调用函数（将里面的东西拿出来）
"""
# 定义函数
'''
def func():
    name = 'Payne'
    print(name)


# 调用
func()
'''

# 闭包的概念(类似于在for循环中for循环)
"""
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j)
"""

# Test1
'''
def func():
    name = 'Payne'
    # print(name)

    def inner():
        name1 = 'Tom'
        print(name1)
    # return inner 返回对象 
    # return inner() 返回函数
    return inner()


func()
'''


def func():
    name = 'Payne'

    # print(name)
    def inner():
        # name1 = 'Tom'
        print(name)

    return inner


f = func()
f()
