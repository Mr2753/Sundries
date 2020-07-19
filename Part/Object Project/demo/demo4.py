# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 1:20
# @Author   :   Payne
# @File     :   demo4.py
# @Software :   PyCharm

class Dog(object):
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

# dog = Dog()
# dog.num = 5
# dog.say()
# print(dog.num)
# My Name is : noName, 旺旺~
# My Name is : noName, 旺旺~
# My Name is : noName, 旺旺~
# My Name is : noName, 旺旺~
# My Name is : noName, 旺旺~

# dog = Dog()
# dog.num = 10
# dog.say()
# Traceback (most recent call last):
#   File "D:/Program Data/PythonProgramData/pycode/^Myself_project^/Part/Object Project/demo/demo4.py", line 45, in <module>
#     dog.num = 10
#   File "D:/Program Data/PythonProgramData/pycode/^Myself_project^/Part/Object Project/demo/demo4.py", line 30, in num
#     raise ValueError("Num must be between 1-6")
# ValueError: Num must be between 1-6
