# -*- coding: utf-8 -*-
# @Time     :   2020/4/7 9:06
# @Author   :   Payne
# @File     :   Basic Selenium.py
# @Software :   PyCharm
import io
import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchAttributeException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
'''
通用方法：
from selenium.webdriver.common.by import By
find_element_by_id 
等价于 find——element（By.ID ,id）
'''

'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 浏览器对象初始化
browser = webdriver.Chrome()
# 用get方法请求网页
browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# Find node or input keys and click
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_first.send_keys('iphone')
time.sleep(1)
button = browser.find_element_by_class_name('btn-search')
button.click()
'''
'''Action chain'''
'''move mouse or Keyboard keys ...
from selenium.webdriver import ActionChains'''
'''
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
'''

# 模拟使用Javascript
'''
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''

# 获取属性 get_attribute (选中节点)
'''
browser = webdriver.Chrome()
url = 'https://dynamic2.scrape.cuiqingcai.com/'
browser.get(url)
logo = browser.find_element_by_class_name('logo-image')
print(logo)
print(logo.get_attribute('src'))
'''

# 获取信息
'''
browser = webdriver.Chrome()
url = 'https://dynamic2.scrape.cuiqingcai.com/'
browser.get(url)
input = browser.find_element_by_class_name('logo-title')
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()
'''

# 切换Frame
'''selenium 打开页面以后，默认在父级Frame里面操作
如果还有子Frame selenium是不能获取到子Frame里面节点的信息
此时需使用switch_to.frame 方法来切换Frame
from selenium.common.exceptions import NoSuchAttributeException'''
'''
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name(' logo')
except NoSuchAttributeException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name(' logo')
print(logo)
print(logo.text)
browser.close()
'''

# 隐式等待与显示等待（如果在selenium没有在dom中找到借鉴将继续等待，超出时间之后泽爆出找不到节点的异常）
'''
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://dynamic2.scrape.cuiqingcai.com/')
input = browser.find_element_by_class_name('logo-image')
print(input)
browser.close()
'''

'''显示等待  from selenium.webdriver.support.ui import WebDriverWait'''
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
browser.close()
'''

'''前进（back）与后退（forward）'''
# 基本页面前进与后退
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
'''

# cookies
'''
browser = webdriver.Chrome()
browser.get('https://www.4399.com')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'https://www.zhihu.com', 'value': 'Payne'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
'''

# 选项卡管理
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')
browser.close()
'''

# 异常捕获
'''
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchAttributeException:
    print('No Element')
finally:
    browser.close()
'''
'''反屏蔽 from selenium.webdriver import ChromeOptions'''

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
# browser = webdriver.Chrome(options=option)
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver",{get:() =>{})'
# })
#
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
#                         {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
# browser.get('https://antispider1.scrape.cuiqingcai.com/')

option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.set_window_size(1366, 768)
browser.get('https://www.baidu.com')
# browser.get_screenshot_as_file('preview.png')
print(browser.page_source)
