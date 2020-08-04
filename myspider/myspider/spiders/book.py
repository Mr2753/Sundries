import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dushu.com']
    start_urls = ['http://www.dushu.com']

    def parse(self, response):
        print(response)
