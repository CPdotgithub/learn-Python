# -*- coding: utf-8 -*-
import scrapy


from scrapy.http.response.html import HtmlResponse  #xpath  css re extract(将htmlresponse转换为列表) extract——first = get

class CsbkSpider(scrapy.Spider):
    name = 'csbk_spider'
    allowed_domains = ['https://www.qiushibaike.com/']  # 允许域名
    start_urls = ['https://www.qiushibaike.com/text/page/1/'] # 开始url
#   html = etree.parse('./test.html', etree.HTMLParser())
    def parse(self, response):  # parse解析response 
        response.xpath('//div[@class="article block untagged mb15 typs_long"]')
        print("="*40)
        print(response)
        print("="*40)
        
