# -*- coding: utf-8 -*-
# @Time     :   2020/4/2 23:25
# @Author   :   Payne
# @File     :   Requests_PyQuery.py
# @Software :   PyCharm
from urllib.parse import urljoin
import requests
from pyquery import PyQuery as pq
import logging
import re

BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def scrape_page(url):
    try:
        response = requests.get(url)
        logging.info(f'response_message: response.status_code {response.status_code} URL:{url}')
        return response.text
    except Exception as e:
        logging.error(f'Error URL {url}, Error message {e}')


def scrape_index(page):
    index_url = f"{BASE_URL}/page/{page}"
    return scrape_page(index_url)


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info(f'Get detail_url {detail_url}')
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def detail_parse(html):
    doc = pq(html)
    cover = doc('img.cover').attr('src')
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


def main(page):
    index_url = scrape_index(page)
    # detail_urls = parse_index(index_url)
    # for detail_url in detail_urls:
    #     detail_html = scrape_detail(detail_url)
        # data = detail_parse(detail_html)
        # logging.info(f"get detail data {data}")


if __name__ == '__main__':
    for page in range(1, 11):
        main(page)
