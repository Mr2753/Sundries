# -*- coding: utf-8 -*-
# @Time     :   2020/4/18 8:14
# @Author   :   Payne
# @File     :   Test3.py
# @Software :   PyCharm


"""类的方法"""

# 类定义


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁 %d。" % (self.name, self.age, self.__weight))


# 实例化类
p = People('Payne', 20, 30)
p.speak()
