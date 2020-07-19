# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 2:09
# @Author   :   Payne
# @File     :   demo7.py
# @Software :   PyCharm

# 多态
class Person:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def printTitle(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("Woman")


class Child(Person):
    def printTitle(self):
        if self.sex == "male":
            print("Boy")
        elif self.sex == "female":
            print("Girl")


May = Child("May", "female")
Peter = Person('Peter', "male")

print(May.name, May.sex, Peter.name, Peter.sex)
May.printTitle()
Peter.printTitle()
