# -*- coding: utf-8 -*-
# @Time     :   2020/3/23 13:42
# @Author   :   Payne
# @File     :   A.py
# @Software :   PyCharm


'''
万物皆对象：
如来： 西游记（如何把经书传给东土大唐） 4个人  各有各自的特征和职能（属性和方法）
类和对象：
    类：笼统泛指（人，动物。。。）
        对象：数据的载体，具体到某个人，事物

'''

'''
面向对象的编程优点：（就是考虑谁来做）
    1、将数据和业务抽象作为对象，有利于程序整体结构的分析和设计 使设计思路更加清晰
    2、业务以对象为单位，对象各自完成工作，减少代码的耦合度，有助于业务的升级和代码的重构
    3、方便工作划分、有利于提高团队的开发效率

'''


class People_Payne:
    def run(self):
        print(f'Running')

    def swim(self):
        print('Swmin')


Payne = People_Payne()
Payne.run()
Payne.swim()
