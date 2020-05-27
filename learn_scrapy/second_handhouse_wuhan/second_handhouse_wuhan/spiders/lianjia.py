# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['https://wh.lianjia.com/']
    start_urls = ['http://https://wh.lianjia.com//']

    def parse(self, response):
        pass
