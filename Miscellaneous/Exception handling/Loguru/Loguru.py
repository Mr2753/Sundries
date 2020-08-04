# -*- coding: utf-8 -*-
# @Time     :   2020/3/27 0:25
# @Author   :   Payne
# @File     :   Loguru.py
# @Software :   PyCharm

from loguru import logger
import os
from urllib.parse import urlencode

# '''基本使用'''
# # logger.add('RunTime.log')
# # logger.debug("This is a message")
#
# '''参数指引'''
# # def add(
# #         self,
# #         sink,
# #         *,
# #         level=_defaults.LOGURU_LEVEL,
# #         format=_defaults.LOGURU_FORMAT,
# #         filter=_defaults.LOGURU_FILTER,
# #         colorize=_defaults.LOGURU_COLORIZE,
# #         serialize=_defaults.LOGURU_SERIALIZE,
# #         backtrace=_defaults.LOGURU_BACKTRACE,
# #         diagnose=_defaults.LOGURU_DIAGNOSE,
# #         enqueue=_defaults.LOGURU_ENQUEUE,
# #         catch=_defaults.LOGURU_CATCH,
# #         **kwargs
# # ):
# #     pass
#
# '''sink'''
# '''format、filter、level'''
# # logger.add('RunTime.log', format="{time} {level} {message}", filter="my_module", level="INFO")
# # logger.debug("This is a message")
#
# '''Del sink'''
# # trace = logger.add('runtime.log1')
# # logger.debug('This is a debug message')
# # logger.remove(trace)
# # logger.debug('This is anthor debug message')
#
# '''Rotation setting'''
# '''
# 通过这样的配置我们就可以实现每 500MB 存储一个文件，每个 log 文件过大就会新创建一个 log 文件。我们在配置 log 名字时加上了一个 time 占位符，这样在生成时可以自动将时间替换进去，生成一个文件名包含时间的 log 文件
# '''
# # logger.add('runtime_{time}.log', rotation="500 MB")
# '''这样就可以实现每天 0 点新创建一个 log 文件输出了。'''
# # logger.add('runtime_{time}.log', rotation="00:00")
# '''配置 log 文件的循环时间，比如每隔一周创建一个 log 文件，写法如下：'''
# logger.add('runtime_{runtime}.log', rotation='1 week')
#
# '''compression setting'''
# # logger.add('runtime.log', compression='zip')
#
# '''string'''
# '''在很多情况下，如果遇到运行错误，而我们在打印输出 log 的时候万一不小心没有配置好 Traceback 的输出，很有可能我们就没法追踪错误所在了。
# 但用了 loguru 之后，我们用它提供的装饰器就可以直接进行 Traceback 的记录，类似这样的配置即可：
# '''
# # logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
# '''Traceback 记录'''
# '''我们用它提供的装饰器就可以直接进行 Traceback 的记录，类似这样的配置即可：'''
# # @logger.catch
# # def my_function(x, y, z):
# #     return 1 / (x + y + z)
# #
# #
# # # my_function(0, 0, 0)
