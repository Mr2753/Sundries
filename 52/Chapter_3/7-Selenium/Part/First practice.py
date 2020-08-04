# -*- coding: utf-8 -*-
# @Time     :   2020/4/7 23:44
# @Author   :   Payne
# @File     :   First practice.py
# @Software :   PyCharm


from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
TOME_OUT = 10
browser = webdriver.Chrome()
wait = WebDriverWait(browser, TOME_OUT)


def scrape_page(url, condition, locator):
    logging.info('Scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('The Time is out %s', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():
    elements = browser.find_elements_by_css_selector('.el-card .el-card__body .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.TAG_NAME, "h2"))


def parse_detail():
    url = browser.current_url
    name = browser.find_element_by_tag_name('h2').text
    categories = [element.text for element in browser.find_elements_by_css_selector('.categories button span')]
    cover = browser.find_element_by_css_selector('.cover').get_attribute('scr')
    score = browser.find_element_by_class_name('score').text
    drama = browser.find_element_by_css_selector('.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def main():
    try:
        for page in range(1, 11):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info('details url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)

    finally:
        browser.close()


if __name__ == '__main__':
    main()
