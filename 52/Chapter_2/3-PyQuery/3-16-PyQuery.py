# -*- coding: utf-8 -*-
# @Time     :   2020/3/17 0:52
# @Author   :   Payne
# @File     :   3-16-3-PyQuery.py
# @Software :   PyCharm

'''
解析文本时将其初始化为一个pyquery 对象
可传入字符串、URL、传入文件名 ...
'''
html ='''
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
from pyquery import PyQuery as pq

doc = pq('https://cuiqingcai.com')
# print(doc('title'))
for item in doc('#container.list li').items():
    print(item)


