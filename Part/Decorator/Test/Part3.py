# -*- coding: utf-8 -*-
# @Time     :   2020/4/17 9:01
# @Author   :   Payne
# @File     :   Test3.py
# @Software :   PyCharm

""" python装饰器语法糖:在python的实际工作中，通常使用@符号来调用装饰器，称之为python语法糖。"""


def decorator1(func):
    def log(*args, **kwargs):
        # do some things here, for example, add some log
        print("function {} was called".format(func.__name__))
        return func(*args, **kwargs)
    return log


# 此时 add = decorator1(add)，add函数就被装饰了
@decorator1
def add(a, b):
    return a + b


# 此时 minus = decorator1(minus)，minus函数被装饰了
@decorator1
def minus(a, b):
    return a - b


# 执行装饰好的add函数，而不再是原来的add函数
print(add(1, 2))
# 执行装饰好的minus函数，而不再是原来的minus函数
print(minus(3, 4))
