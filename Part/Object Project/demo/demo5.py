# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 1:40
# @Author   :   Payne
# @File     :   demo5.py
# @Software :   PyCharm

#  类与对象的动态性、混入机制
# 在python中开头动态的为自定义或对象添加数据成员和成员方法，这是python动态类型的一种重要体现
import types


class Dog:
    total = 0

    def __init__(self, name="noName", num=3):
        self.name = name
        self.__num = num
        self._shout = ""
        Dog.total += 1

    def say(self):
        for i in range(self.__num):
            self._shout = ", 旺旺~"
            print(f"My Name is : {self.name + self._shout}")

    @property
    # property装饰器可以将方法转为属性
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise ValueError("Num must be an integer!")
        if value < 0 or value > 6:
            raise ValueError("Num must be between 1-6")
        self.__num = value


def setRun(self, r):
    self.speed = r


d = Dog()
# d.color = 'red'
# print(d.color)

d.setRun = types.MethodType(setRun, d)
d.setRun(20)
print(d.speed)
