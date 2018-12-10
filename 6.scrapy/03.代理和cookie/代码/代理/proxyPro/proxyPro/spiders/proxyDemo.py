# -*- coding: utf-8 -*-
import scrapy


class ProxydemoSpider(scrapy.Spider):
    name = 'proxyDemo'
    #allowed_domains = ['www.baidu.com/s?wd=ip']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        fp = open('proxy.html','w',encoding='utf-8')
        fp.write(response.text)
