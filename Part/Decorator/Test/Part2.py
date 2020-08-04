# -*- coding: utf-8 -*-
# @Time     :   2020/4/17 8:57
# @Author   :   Payne
# @File     :   Part1.py
# @Software :   PyCharm


"""基础装饰器"""


# 定义了一个函数对象
def add(a, b):
    return a + b


# my_add引用了这个函数对象(赋值（此处类似于改名字）)
my_add = add


# 定义了一个函数对象decorator1，所需参数也是一个函数对象
def decorator1(func):
    # 在函数内又定义了一个新的函数对象log
    def log(*args, **kwargs):
        return func(*args, **kwargs)

    # 返回这个log函数对象
    return log


# 调用函数decorator1，并将my_add作为参数传入，同时将返回的对象赋值给my_decorator, 可知，这里返回的是log函数，也就是说，此时my_decorator指向了log函数
my_decorator = decorator1(my_add)
# 调用my_decorator函数，即调用内部的log函数
print(my_decorator(1, 2))


@decorator1
def func(a, b):
    return a + b


print(func(1, 1))
