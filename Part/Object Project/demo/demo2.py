# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 0:23
# @Author   :   Payne
# @File     :   demo2.py
# @Software :   PyCharm

# 私有成员在类的外部不能直接访问，一般是在类的内部进行访问和操作，
# 共有成员可以公开使用，既可以在类的内部进行访问，也可以在外部程序中使用

class Dog(object):
    total = 0  # 类的成员

    def __init__(self, name="anonymous", num=3):
        self.name = name  # 公有成员
        self.__num = num  # 私有成员
        self._shout = ""  # 保护成员
        Dog.total += 1

    def say(self):
        for i in range(self.__num):
            self._shout += ", 汪汪~"
            """这是小狗的沟通方法"""
        print(f"我的名字是： {self.name + self._shout}")


dog = Dog()
dog.say()

# “_xx”:
# 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如：当使用“from M import”时，不会将以一个下划线开头的对象引入


# "__xx":
# 以双下划线的表示时私有属性的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在foobar内部，__boo变成_foobar__boo,如self._foobar__boo）


# __xx__:
# 定义的时特例方法。用户控制的命名空间内的变量或是属性，如init，__import__,file。只有当文档有说明使用，不要自己定义这类变量。（就是说这些事python内部定义的变量名）

# python中类成员：
# 数据成员：静态字段 普通字段
# 成员方法：静态方法 类方法 普通方法
# 特性/属性： 普通特性
