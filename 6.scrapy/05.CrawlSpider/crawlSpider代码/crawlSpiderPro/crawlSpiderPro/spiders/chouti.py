# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    #allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com/']

    #实例化了一个链接提取器对象
    #链接提取器：用来提取指定的链接（url）
    #allow参数：赋值一个正则表达式
    #链接提取器就可以根据正则表达式在页面中提取指定的链接
    #提取到的链接会全部交给规则解析器
    link = LinkExtractor(allow=r'/all/hot/recent/\d+')
    rules = (
        #实例化了一个规则解析器对象
        #规则解析器接受了链接提取器发送的链接后，就会对这些链接发起请求，获取链接对应的页面内容，就会根据指定的规则对页面内容中指定的数据值进行解析
        #callback：指定一个解析规则（方法/函数）
        #follow:是否将链接提取器继续作用到连接提取器提取出的链接所表示的页面数据中
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)

