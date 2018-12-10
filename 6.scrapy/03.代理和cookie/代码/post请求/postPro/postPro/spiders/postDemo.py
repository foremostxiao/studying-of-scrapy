# -*- coding: utf-8 -*-
import scrapy

#需求：百度翻译中指定词条对应的翻译结果进行获取
class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']
    #该方法其实是父类中的一个方法：该方法可以对star_urls列表中的元素进行get请求的发送
    #发起post：
        #1.将Request方法中method参数赋值成post
        #2.FormRequest()可以发起post请求（推荐）
    def start_requests(self):
        print('start_requests()')
        #post请求的参数
        data = {
            'kw': 'dog',
        }
        for url in self.start_urls:
            #formdata:请求参数对应的字典
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)
