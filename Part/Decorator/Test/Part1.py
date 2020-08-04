# -*- coding: utf-8 -*-
# @Time     :   2020/4/17 8:46
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm


# 定义了一个函数对象
def add(a, b):
    return a + b


# my_add引用了这个函数对象
my_add = add


def decorator1(func):  # 定义了一个函数对象decorator1，所需参数也是一个函数对象
    def log(*args, **kwargs):  # 在函数内又定义了一个新的函数对象log
        return func(*args, **kwargs)

    return log  # 返回这个log函数对象


# 调用函数decorator1，并将my_add作为参数传入，同时将返回的对象赋值给mydecorator, 可知，这里返回的是log函数，
# 也就是说，此时mydecorator指向了log函数
mydecorator = decorator1(my_add)
# 调用mydecorator函数，即调用内部的log函数

print(mydecorator(1, 2))
