# -*- coding: utf-8 -*-
# @Time     :   2020/6/20 15:18
# @Author   :   Payne
# @File     :   demo8.py
# @Software :   PyCharm

# 构造方法 、析构方法
'''
# __init__ 构造方法：这个方法在创建对象时就会访问，也即：类后面在（）调用执行init方法
# __del__（self）：    恰好在对象要被删除之前调用，不用专门写，系统会自动调用

# class Function:
#
#     def __init__(self, name):
#         print(f"执行init方法: {name}")
#
#     @staticmethod
#     def Show():
#         print("Show 方法")
#
#
# obj = Function(name="init")
'''


# __add__(self, other)方法

class Func1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        temp = "%s-%s" % (self.name, other.name)
        return temp


obj1 = Func1("aaa", 123)
obj2 = Func1('bbb', 456)
print(f"对象1 {obj1}")
print(f"对象2 {obj2}")
print('——自动执行add方法——')
ret = obj1+obj2     # self 代表obj1，other代表obj2
print("add 方法: ", ret)
