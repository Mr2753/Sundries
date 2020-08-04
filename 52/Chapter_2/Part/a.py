# -*- coding: utf-8 -*-
# @Time     :   2020/4/6 2:31
# @Author   :   Payne
# @File     :   a.py
# @Software :   PyCharm
import re
from urllib.parse import urljoin

import requests
from pyquery import PyQuery as pq
from loguru import logger
import logging
import pymongo

BASE_URL = 'https://static1.scrape.cuiqingcai.com'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['movies']
collection = db['movie']


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('Got detail_url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
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


def save_data(data):
    data = collection.update_one(
        {
            'name': data.get('name')
        }, {
            '$set': data
        },
        upsert=True
    )
    logging.info('The save to Mongo Object ID %s', data)


@logger.catch
def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('Save data to Mongo')
        save_data(data)
        logging.info('Successfully saved')


if __name__ == '__main__':
    for page in range(1, 11):
        main(page)
