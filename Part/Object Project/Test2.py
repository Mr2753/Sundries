# -*- coding: utf-8 -*-
# @Time     :   2020/4/18 8:07
# @Author   :   Payne
# @File     :   Test2.py
# @Software :   PyCharm


"""类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用"
类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。如下实例化类 MyClass，对应的 __init__() 方法就会被调用:
"""


class Complex:
    def __init__(self, real_part, image_part):
        self.r = real_part
        self.i = image_part


x = Complex(3.0, -4.5)
print(x.r, x.i)
