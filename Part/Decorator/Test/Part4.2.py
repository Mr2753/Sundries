# -*- coding: utf-8 -*-
# @Time     :   2020/4/17 9:08
# @Author   :   Payne
# @File     :   Part4.2.py
# @Software :   PyCharm


"""多重装饰"""
from functools import wraps


def decorator1(func):
    @wraps(func)
    def log(*args, **kwargs):
        # do some things here, for example, add some log
        print("function {} was called in decorator1".format(func.__name__))
        return func(*args, **kwargs)

    return log


def decorator2(func):
    @wraps(func)
    def another_log(*args, **kwargs):
        # do some things here, for example, add some log
        print("function {} was called in decorator2".format(func.__name__))
        return func(*args, **kwargs)

    return another_log


@decorator1
@decorator2
def add(a, b):
    return a + b


add(1, 2)


@decorator2
@decorator1
def minus(a, b):
    return a - b


minus(3, 4)
