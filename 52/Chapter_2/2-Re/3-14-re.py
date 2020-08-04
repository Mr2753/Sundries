#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

'''
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：re.search(pattern, string, flags=0)
'''
# a = 'hello, my name is Payne number is 089076-8789 and email is 12/8x6901Xx@qq.com, and my website is httPs://www.abcder123f.com'
# b1 = re.search('[a-zA-Z]+://[\S]+',a)
# b2= re.search('[a-zA-Z]+://[^\s]+',a)
# b3 = re.search('[0-z_]+:.*',a)
# b4 = re.search('[0-z]+:.*',a)

# print(b1)
# print(b2)
# print(b3)
# print(b4)
'''拓展'''
a = 'hello, my name is Payne number is 089076-8789 and email is 12/8\'x6901Xx@qq.com, and my website is httPs://www.abcder123f.com'
c = re.search('[0-z]+\.\w+', a)
c1 = re.search('[""-z]+\.\w+', a)
# print(c1)
# h = 'abcdefghijknmopqrAst9uvwXyz'
# print(re.search('^"http[!-z]+',h))
# print(re.search('1.*',a))
# print(re.search('.+\s$',a))
'''
本段小计，易混淆处
. 匹配 0 个或多个表达式   
+ 匹配 1 个或多个表达式
'''

'''
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
函数语法：re.match(pattern, string, flags=0)
group(num=0)匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的  元组  ，从 1 到 所含的小组号。
'''
ma = "Hello 123 456 Word_This is a Regex Demo asd"
# print(len(ma))
# result1 = re.match('^Hello \s\d\d\d\s\d{4}\s\w{10}',ma)
result2 = re.match('^Hello\s(\d+)\s\d+\s\w+', ma)
result3 = re.match('^Hello.*?(\d+).*asd$', ma)
# print(result2)
# print(result2.group())
# print(result2.span())
# print(result3)
'''
re.sub
语法：
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

sub = re.sub('\d+', '', ma)
# print(sub)
'''
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
语法格式为：
re.compile(pattern[, flags])
参数：
pattern : 一个字符串形式的正则表达式
flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
'''

date1 = '2019-1-2 12:20'
date2 = '2019-1-5 17:20'
date3 = '2019-1-9 14:20'

pattern = re.compile('\d+:\d+')
result_1 = re.sub(pattern, '', date1)
result_2 = re.sub(pattern, '', date2)
result_3 = re.sub(pattern, '', date3)
# print(result_1, result_2, result_3)
a = 'hello, my name is Payne number is 089076-8789 and email is 12/8\'x6901Xx@qq.com, and my website is httPs://www.abcder123f.com'
print(type(a))
ids = re.findall('hello(.*?)name', a)
print(ids)
