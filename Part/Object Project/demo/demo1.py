# -*- coding: utf-8 -*-
# @Time     :   2020/6/18 17:06
# @Author   :   Payne
# @File     :   demo1.py
# @Software :   PyCharm

class Dog(object):

    def say(self):
        print("汪汪汪~")


# slef，它的作用是对于自身对象的引用
dog = Dog()
dog.say()


