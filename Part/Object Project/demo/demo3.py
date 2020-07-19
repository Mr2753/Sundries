# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 0:53
# @Author   :   Payne
# @File     :   demo3.py
# @Software :   PyCharm

# 数据成员
# 1\属于对象的数据成员,一般构造在构造方法
# __init__()定义,当然也可以在其他成员方法中定义,在定义和使用时以self作为前缀,同一类的不同对象的数据成员之间互不影响.只能通过对象名进行访问


# 2\属于类的数据成员,
# 是该类所有对象的共享的,不属于任何一个对象,在定义类时这类数据成员一般不以任何一个成员方法的定义中.可以通过类名或对象名访问

# 在demo2中,total就是属于类的数据成员,name\__num和_shout都是属于对象的数据成员

# 成员方法\ 类方法\ 静态方法\ 抽象方法
# 对象用来描述对象所具有的行为.在python类的成员方法可以粗略分为四大类:公有方法\私有方法\静态方法\类方法

# 私有方法:
# 以两个下划线开始. 每个对象都有自己的公有方法和私有方法,在这两类方法中都可以访问数据类和对象的成员.

# 公有方法通过对象名直接调用
# 私有方法不能通过对象名直接调用，只能在实例方法中通过self调用或者外部通过python支持的特殊方法调用

# 抽象类和抽象方法：
# 由于python没有抽象类、接口的概念，所以需要实现这种功能得abc。py这个库

# 抽象类
import abc
from abc import ABC, abstractclassmethod


# 抽象类
# noinspection PyDeprecation
class Foo(metaclass=abc.ABCMeta):
    # 抽象方法
    @abstractclassmethod
    def exec(self):
        pass


# 实体类
class A(Foo):
    def exec(self):  # 重写exec方法
        pass
