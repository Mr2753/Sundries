# -*- coding: utf-8 -*-
# @Time     :   2020/4/17 9:06
# @Author   :   Payne
# @File     :   Part4.1.py
# @Software :   PyCharm


"""带参数的装饰器"""


def decorator2(my_string):
    print(my_string)

    def decorator1(func):
        def log(*args, **kwargs):
            # do some things here, for example, add some log
            print("function {} was called".format(func.__name__))
            return func(*args, **kwargs)

        return log

    return decorator1


@decorator2("Used decorator here")
def add(a, b):
    return a + b


@decorator2("Used decorator here")
def minus(a, b):
    return a - b


print(add(1, 2))
print(minus(3, 4))
