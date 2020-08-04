# -*- coding: utf-8 -*-
# @Time     :   2020/3/30 18:53
# @Author   :   Payne
# @File     :   logure.py
# @Software :   PyCharm

from loguru import logger


@logger.catch
def my_function(x, y, z):
    return 2 / (x + y + z)


print(my_function(0, 0, 0))

