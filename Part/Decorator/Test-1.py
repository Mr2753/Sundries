# -*- coding: utf-8 -*-
# @Time     :   2020/4/2 21:24
# @Author   :   Payne
# @File     :   Test-1.py
# @Software :   PyCharm


# 闭包
"""
在了解装饰器之前，我们需要知道什么是闭包？
在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
"""

'''
def test(number):
    def test_in(number_in):
        print(f"Test_in  {number_in}")
        return number_in + number

    # 返回闭包的结果
    return test_in


ret = test(20)
print(ret(100))
'''
'''实际闭包例子'''

'''
def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(1, 5)
print(line1(5))
print(line2(5))
'''

# Decorator
'''装饰器是程序开发中经常用到的一个功能，用好了装饰器，开发效率如虎添翼。'''
'''1-明白函数怎么执行的'''
'''
def foo():
    print("foo")


# foo  # 表示函数
foo()  # 表示执行函数
# 函数名仅仅是个变量, 只不过指向了定义的函数,可以通过函数名() 调用函数
'''

'''Decorator'''


def make_html(fn):
    def W_append():
        return "html" + fn() + "html"

    return W_append


@make_html
def test1():
    return "|hello|"


print(test1())
