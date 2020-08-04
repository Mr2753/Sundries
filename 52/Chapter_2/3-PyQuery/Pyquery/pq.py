#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
基本CSS選擇器 如果是id属性,前面加#。
# 如果是class属性 加.
# 标签什么也不加
# 单冒号(:)用于CSS3伪类，双冒号(::)用于CSS3伪元素
'''
import io
import sys
import requests
from pyquery import PyQuery as pq

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# start_url = 'https://maoyan.com/board/4?offset=2'
# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
# }
#
# response = requests.get(start_url, headers=header)
#
# html = response.text

# print(html)
# 字符串初始化
# doc = pq(html)
# print(doc('dd'))

# URL初始化
# doc = pq('https://www.baidu.com')
# print(doc('head'))
html = '''
<body>
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">Second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">Third item</span> </a> </li>
            <li class="item-1 active"><a href="link4.html">Fourth item</a> </li>
            <li class="item-0"><a href="link5.html">Fifth item</a> </li>
        </ul>
    </div>
</body>
</html>
'''
print(html)
# 字符串初始化
'''
doc = pq(html)
print(doc('li'))
'''

# URL初始化
'''
doc = pq(url='https://www.baidu.com')
print(doc('head'))
'''

# 文件初始化
'''
doc = pq(filename='html-.html')
print(doc('li'))
'''

'''
doc = pq(html)
print(doc('.list li'))
'''

# A、查找元素
#   a子元素
'''
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
print('*'*80)
lis = items.find('li')
print(type(lis))
print(lis)
print('*'*80)
lis = items.children()
print(type(lis))
print(lis)
lis = items.children('.active')
print(type(lis))
print(lis)
'''
#   b父元素
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

parent = items.parents('#container')
print(parent)
'''
#   c兄弟元素
'''
doc = pq(html)
li = doc('.item-0.active').siblings()
print(li)
'''

# B\遍历

'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
'''

# 循环遍历获取html

doc = pq(html)
lis = doc('li').items()  # items()生成产生器
# print(lis)
for li in lis:
    print(li)

# 获取属性
'''
doc = pq(html)
a = doc('.item-0.active a')
b = doc('.item-0.active a').attr('href')
print(a)
print(b)
print(a.attr('href'))
'''
# 获取文本
'''
doc = pq(html)
a = doc('.item-0.active').text()
print(a)
'''

# 获取HTML
'''
doc = pq(html)
a = doc('.item-0.active')
print(a)
print(a.html())
'''

# DOM操作 remove_class(del) add_class(add)
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)
'''

# attr\css offset Add or Del
'''
dac = pq(html)
li = dac('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.css offset('font-size','14px')
print(li)
'''

html1 = '''
    <div class="wrap">
        Hello world
        <p>This is a paragraph</p>
    </div>
'''
# 单独获取Hello world 先删除<p> 后提取div
'''
doc = pq(html1)
wrap = doc('.wrap')
print(wrap.text())
print('^'*10)
a = wrap.find('p').remove_class('p')
print(a.text())
'''

# 伪类选择器
'''
doc = pq(html)
li1 = doc('li:first-child')
# print(li1)
li2 = doc('li:last-child')
# print(li2)
li3 = doc('li:nth-child(2)')
# print(li3)
li4 = doc('li:gt(2)')
# print(li4)    #   第三个标签后的标签
li5 = doc('li:nth-child(2n)')
# print(li5)      #   偶数标签
li6 = doc('li:contains(second')
print(li6)      #   包含second文本的
'''
