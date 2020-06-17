#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''lambda 函数  lambda （形参）x ：（返回）2*x +1'''
'''
def ds(s):
    return 2*s + 1
print(ds(5))
'''

'''
g = lambda x: 2*x +1
print(g(1))
'''

'''
v= lambda s,a : s + a
print(v)
'''

# print(help(filter))  筛选为 True的结果输出
'''
class filter(object):
|  filter(function or None, iterable) --> filter object
|  
|  Return an iterator yielding those items of iterable for which function(item)
|  is true. If function is None, return the items that are true.
|  
|  Methods defined here:
|  
|  __getattribute__(self, name, /)
|      Return getattr(self, name).
|  
|  __iter__(self, /)
|      Implement iter(self).
|  
|  __next__(self, /)
|      Implement next(self).
|  
|  __reduce__(...)
|      Return state information for pickling.
|  
|  ----------------------------------------------------------------------
|  Static methods defined here:
|  
|  __new__(*args, **kwargs) from builtins.type
|      Create and return a new object.  See help(type) for accurate signature.

'''
# 假如 第一个为True 则继续匹配可迭代中的下一个为True的结果 否则 从第二开僧
'''
b = filter(None,[1,0,False,True])
a = list(b)
print(a)
'''

'''
def odd(x):
    return x % 2
temp = range(100)
show = list(filter(odd,temp))
print(show)

odds = list(filter(lambda x: x%2,range(100)))
print(odds)

'''

'''
maps = list(map(lambda x:x+1,range(10)))
print(maps)
'''

'''递归,不断调用自己'''

# def a(n):
#     a = n
#     for i in range(1,n):
#         a *= i
#     return a
''''''
# def a(n):
#     if n == 1:
#         return 1
#     else:
#         return n*a(n-1)
# print(a(5))

'''斐波那契数列'''
'''
 n = 1 F = 1
 n = 2 F = 1
 n = 3 F = F(n-1)+F(n - 2)
'''

'''
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        return -1
    while (n-2)>0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
while True:
    c = fab(int(input('请输入月份:')))
    print(f'总共有 {c} 对')
'''

# def fab(n):
#     if n < 1:
#         return -1
#     if n == 1 or n ==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# print(fab(20))

# 练习
'''递归'''


def a(n):
    a = n
    for i in range(1, n):
        # print(i)
        a += i
    return a


print(a(3))
