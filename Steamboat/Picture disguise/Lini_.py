# -*- coding: utf-8 -*-
# @Time     :   2020/3/27 16:36
# @Author   :   Payne
# @File     :   Lini_.py
# @Software :   PyCharm

import io
import requests
from urllib.parse import urljoin
from parsel import Selector

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

url = 'http://www.porters.vip/confusion/recruit.html#'
resp = requests.get(url)
# print(resp.text)
sel = Selector(resp.text)
image_name = sel.css('.pn ::attr(src)').get()
image_url = urljoin(url, image_name)
image_body = requests.get(image_url).content
image_stream = Image.open(io.BytesIO(image_body))
print(pytesseract.image_to_data(image_stream))

print(pytesseract.image_to_string(image_stream))

