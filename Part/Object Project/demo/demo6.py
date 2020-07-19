# -*- coding: utf-8 -*-
# @Time     :   2020/6/19 1:49
# @Author   :   Payne
# @File     :   demo6.py
# @Software :   PyCharm

# 继承、多态


# 在OPP（object Oriented Programing）程序设计中，我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称之为字类，而被继承的class称之为积累、父类、超类

# 设计一个新类时，如果可以继承一个已有的设计良好的类，然后进行二次开发，可以大幅度减少开发工作量，并且可以很大程度上保证质量。
# 在继承关系中，字类可以继承父类的公有成员。但是不能继承父类的私有成员。如果需要在派生类中调用基类的方法，可以使用内置函数super（）或者通过“基类名。方法名（）"的方式来实现这个目的
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def printTitle(self):
        if self.sex == "Male":
            print("This is Man")
        elif self.sex == "female":
            print("Woman")
        else:
            print("Error")


class Child(Person):
    pass


May = Child("May", "female")
Peter = Person('Peter', "Male")

print(May.name, May.sex, Peter.name, Peter.sex)
May.printTitle()
Peter.printTitle()

