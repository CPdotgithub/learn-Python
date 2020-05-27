# -*- coding: utf-8 -*-
import scrapy


class StockinfoSpider(scrapy.Spider):
    name = 'stockinfo'
    allowed_domains = ['http://quote.eastmoney.com/stocklist.html']
    start_urls = ['http://http://quote.eastmoney.com/stocklist.html/']

    def parse(self, response):
        pass
