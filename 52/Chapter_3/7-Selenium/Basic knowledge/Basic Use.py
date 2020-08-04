#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
'''
# 一、基本使用
browser = webdriver.Chrome()
try:
    # 打开百度浏览器
    browser.get('https://www.baidu.com')
    # 通过ID找出来里面kw的元素
    input = browser.find_element_by_id('kw')
    # 输入键
    input.send_keys('Python')
    # 敲入回车
    input.send_keys(Keys.ENTER)
    # 等待某个元素被加载出来  content_left
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # 打印出来当前的URL cookie值 源代码
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)

finally:
    # 关闭浏览器
    browser.close()
'''
# 一、基本使用
# 声明浏览器对象
'''
from selenium import webdriver
# 谷歌
browser = webdriver.Chrome()
# 火狐
browser = webdriver.Firefox()
# Edge
browser = webdriver.Edge()

browser = webdriver.PhantomJS()

browser = webdriver.Safari()

'''

# 访问网页面
'''
from selenium import webdriver

# 打开浏览器
browser = webdriver.Chrome()
# 进入访问的连接
browser.get('url')
# 打印网页源代码
print(browser.page_source)
# 关闭浏览器
browser.close()
'''

# 查找元素 单个元素 多个元素在element后加s即可
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()

# browser.find_element_by_name()
# browser.find_element_by_xpath()
# browser.find_element_by_link_text()
# browser.find_element_by_link_text()
# browser.find_element_by_tag_name()
# browser.find_element_by_class_name()
# browser.find_elements_by_css_selector()

# 通用查找方式
from selenium import webdriver
from selenium.webdriver.common.by import By     # 通用查找方式库
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID,'q')
print(input_first)
browser.close()
'''

# 二、元素交互操作
# 对元素调用交互方法
'''
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('IPone')
time.sleep(1)
input.clear()
input.send_keys('IPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
'''

# 交互动作  #  将动作附加到动作链中串行执行
'''
from selenium import webdriver
from selenium.webdriver import ActionChains  #

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
'''

# 执行JavaScript 从开始滑倒底实例
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''

# 三\ 获取元素信息
# 1\获取属性
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('special')
print(logo)
print(logo.get_attribute('class'))
"""

# 2\获取文本值
"""
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.baidu.com/'
browser.get(url)
input = browser.find_elements_by_class_name('special')
print(input.text)
"""

# 3\获取id 位置\标签名\大小
"""
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.baidu.com/'
browser.get(url)
input = browser.find_elements_by_class_name('submit')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
"""

# 四\ Frame
'''
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchAttributeException:
    print('No logo')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
'''

# 五\等待
# 隐式等待
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('xxxx')
# print(input)
"""

# 显示等待
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located(By.ID, 'q'))
button = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, 'btn-search'))
print(input, button)
"""

# 六、前进后退
"""
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com/')
browser.get('https://www.360.cn/')
browser.back()
time.sleep(2)
browser.forward()
browser.close()
"""

# 七、cookies
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/')
print(browser.get_cookies())
browser.add_cookie({
    'name':'name',
    'domain':'www.zhihu.com',
    'value':'germey',
})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
"""

# 八、选项卡
"""
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.360.cn/')
"""

# 九、异常处理
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')
"""


"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchAttributeException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
"""


