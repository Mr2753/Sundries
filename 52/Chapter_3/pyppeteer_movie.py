import asyncio
import json
import os

from urllib.parse import urljoin

from pyquery import PyQuery as pq
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(message)s")
INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{}'
DETAIL_URL = 'https://dynamic2.scrape.cuiqingcai.com/detail/'
TOTAL_PAGE = 10
TIMEOUT = 10
width, height = 1366, 768
MOVIE_DIR = 'pyppeteer_movie'
os.path.exists(MOVIE_DIR) or os.mkdir(MOVIE_DIR)


# https://github.com/miyakogi/pyppeteer/pull/160/files
async def fetch(url, selector):
    try:
        await tab.goto(url)
        logging.info("scraping url : %s", url)
        await tab.waitForSelector(selector=selector,
                                  options={
                                      'timeout': TIMEOUT * 1000
                                  })
        return await tab.content()
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)


# 从索引页获取详情页链接
async def scrape_index(page):
    url = INDEX_URL.format(page)
    selector = '#index .name'
    doc = pq(await fetch(url, selector))
    a_tag_list = doc('#index .name').items()
    return [_.attr('href') for _ in a_tag_list]


# 获取详细数据
async def scrape_detail(short_url):
    url = urljoin(DETAIL_URL, short_url)
    selector = 'h2'
    doc = pq(await fetch(url, selector))
    title = doc('a h2').text().split('-')[0].strip()
    score = doc('.score').text()
    categories = doc('.categories').text()
    info = doc('.item .info span').text()
    drama = doc('.drama p').text()
    director = doc('.directors p').text()
    actors = doc('.actors div').text()
    movie_dict = {
        'title': title,
        'score': score,
        'categories': categories,
        'info': info,
        'drama': drama,
        'director': director,
        'actors': actors
    }
    await save_data(movie_dict)


async def save_data(movie_dict):
    logging.info("movie_dict: %s", movie_dict)
    title = movie_dict.get('title')
    with open(f'{MOVIE_DIR}/{title}.json', 'w', encoding='utf-8') as f:
        json.dump(movie_dict, f, ensure_ascii=False, indent=2)


async def init():
    global browser, tab
    executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
    browser = await launch(headless=True, executablePath=executablePath,
                           args=['--disable-infobars',
                                 f'--window-size={width},{height}'])
    # executablePath = r'C:\Users\W\AppData\Local\Google\Chrome\Application\chrome.exe'
    # browser = await launch(
    #     {'executablePath': executablePath,
    #      'headless': False, 'slowMo': 30,
    #      })
    tab = await browser.newPage()
    await tab.setViewport({'width': width, 'height': height})
    await tab.evaluateOnNewDocument('Object.defineProperty('
                                    'navigator, "webdriver", {get: () => undefined})')


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            index_url_list = await scrape_index(page)
            for short_url in index_url_list:
                await scrape_detail(short_url)

    finally:
        await browser.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop().run_until_complete(main())

