# -*- coding: utf-8 -*-
# @Time     :   2020/4/18 1:00
# @Author   :   Payne
# @File     :   Test1.py
# @Software :   PyCharm


class Class(object):
    i = 123456

    def f(self):
        return 'Hello World'


x = Class()
print(x.i)
print(x.f())
