# -*- coding: utf-8 -*-
import scrapy


class PicSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'pic_spider'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']

    def parse(self, response):
        print(response.text)
