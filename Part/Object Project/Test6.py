# -*- coding: utf-8 -*-
# @Time     :   2020/4/18 8:33
# @Author   :   Payne
# @File     :   Test6.py
# @Software :   PyCharm


# 定义父类
class Parent:
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
