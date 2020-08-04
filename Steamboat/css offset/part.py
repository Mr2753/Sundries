# -*- coding: utf-8 -*-
# @Time     :   2020/4/8 8:46
# @Author   :   Payne
# @File     :   part.py
# @Software :   PyCharm

import requests
import re
from parsel import Selector

url = 'http://www.porters.vip/confusion/flight.html'
response = requests.get(url)
sel = Selector(response.text)
em = sel.css('em.rel').extract()
for element in em:
    element = Selector(element)
    # 定位所有的<b>标签
    element_b = element.css('b').extract()
    b1 = Selector(element_b.pop(0))
    # 获取第一对<b>标签的值
    base_price = b1.css('i::text').extract()
    alternate_prices = []
    for eb in element_b:
        eb = Selector(eb)
        # 提取<b>标签的style属性值
        style = eb.css('b::attr("style")').get()
        # 获取具体的位置
        position = ' '.join(re.findall('left:(.*)px', style))
        # 获得该标签下数字
        value = eb.css('b::text').get()
        alternate_prices.append({'position': position, 'value': value})
        for al in alternate_prices:
            position = int(al.get('position'))
            value = al.get('value')
            # 判断位置是否正确
            plus = True if position >= 0 else False
            # 计算下标以16px为基准
            index = int(position / 16)
            base_price[index] = value
    print(base_price)

