# -*- coding: utf-8 -*-
# @Time     :   2020/4/27 10:34
# @Author   :   Payne
# @File     :   Basic User 427.py
# @Software :   PyCharm
import io
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 通用选择方法
from selenium.webdriver import ActionChains  # 动作链
from selenium.common.exceptions import NoSuchAttributeException  # 异常捕获
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    # 判断一个元素是否存在
from selenium.webdriver import ChromeOptions

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

BaiDu_url = 'https://www.baidu.com'
TaoBao_url = 'https://www.taobao.com/'
ZhiHu_url = 'https://www.zhihu.com/explore'
Scraping_url = 'https://dynamic2.scrape.cuiqingcai.com/'
Frame_url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
'''基本使用与选择器'''
# browser = webdriver.Chrome()
# browser.get(TaoBao_url)
# # 打印网页源代码
# # print(browser.page_source)
# # browser.close()
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# input_fourth = browser.find_element(By.ID, 'q')
# print(input_first, '\n')
# print(input_second, '\n')
# print(input_third, '\n')
# print(input_fourth, '\n')


'''节点交互'''
# browser = webdriver.Chrome()
# browser.get(TaoBao_url)
# input = browser.find_element_by_id('q')
# input.send_keys('iPhon')
# time.sleep(1)
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()


'''动作链'''
# browse = webdriver.Chrome()
# run_oob_url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browse.get(run_oob_url)
# browse.switch_to.frame('iframeResult')
# source = browse.find_element_by_css_selector('#draggable')
# target = browse.find_element_by_css_selector('#droppable')
# actions = ActionChains(browse)
# actions.drag_and_drop(source, target)
# actions.perform()


'''执行JavaScript'''
# browser = webdriver.Chrome()
# browser.get(ZhiHu_url)
# print(browser.page_source)
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
# browser.close()


'''获取节点信息'''
'''
/get_attribute获取节点属性，前提是选中这个节点
/text 获取文本信息
'''
# browser = webdriver.Chrome()
# browser.get(Scraping_url)
# logo = browser.find_element_by_class_name('logo-image')
# print(logo)
# print(logo.get_attribute('src'))
# input = browser.find_element_by_class_name('logo-title')
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


'''切换Frame'''
'''
switch_to.frame
方法来切换Frame
'''
# browser = webdriver.Chrome()
# browser.get(Frame_url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchAttributeException:
#     print("NO LOGO")
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


'''延时等待'''
# 一、隐式等待
'''如果selenium没有在DOM中找到节点将继续等待，
超出设定时间后，则抛出找不到节点异常'''
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get(Scraping_url)
# input = browser.find_element_by_class_name('logo-image')
print(input)
# 二 显示等待
'''指定要查找的节点，然后指定一个最长的等待时间'''
# browser = webdriver.Chrome()
# browser.get(TaoBao_url)
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)


'''页面前进(forward)与后退(back)'''
# browser = webdriver.Chrome()
# browser.get(TaoBao_url)
# browser.get(ZhiHu_url)
# browser.get(Scraping_url)
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


'''Cookies'''
# browser = webdriver.Chrome()
# browser.get(ZhiHu_url)
# print(browser.get_cookies())
# browser.add_cookie({'name': 'Payne'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


'''选项卡管理'''
# browser = webdriver.Chrome()
# browser.get(BaiDu_url)
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.driver.switch_to_window(browser.window_handles[1])
# browser.get(TaoBao_url)
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get(Scraping_url)


'''反屏蔽'''
'''
使用JavaScript直接把webdriver属性置空 Object.defineProperty(navigator,"webdriver", {get:() => undefined})
但在此之前以对webdriver进行了检测
'''
'''
使用CDP即（即Chrome Devtools-Protocol，chrome开发者工具协议）,来解决这个问题
执行CDP的方法叫page.addScriptToEvaluateOnNewDocument 然后传入上文的JavaScript代码即可
'''

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
# print(browser.page_source)

'''无头模式'''
# option = ChromeOptions()
# option.add_argument('--headless')
# browser = webdriver.Chrome(options=option)
# browser.set_window_size(1366, 768)
# browser.get(BaiDu_url)
# print(browser.page_source)
