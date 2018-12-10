# -*- coding: utf-8 -*-
import scrapy
from moviePro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    #allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie']

    #专门用于解析二级子页面中的数据值
    def parseBySecondPage(self,response):
        actor = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/text()').extract_first()
        language = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/text()').extract_first()
        longTime = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[8]/td[2]/text()').extract_first()

        #取出Request方法的meta参数传递过来的字典(response.meta)
        item = response.meta['item']
        item['actor'] = actor
        item['language'] = language
        item['longTime'] = longTime
        #将item提交给管道
        yield item
    def parse(self, response):
        #名称，类型，导演，语言，片长
        div_list = response.xpath('/html/body/div[1]/div[1]/div[2]/div')
        for div in div_list:
            name = div.xpath('.//div[@class="meta"]/h1/a/text()').extract_first()
            #如下xpath方法返回的是一个列表，切列表元素为4
            kind = div.xpath('.//div[@class="otherinfo"]//text()').extract()
            #将kind列表转化成字符串
            kind = "".join(kind)
            url = div.xpath('.//div[@class="meta"]/h1/a/@href').extract_first()

            print(kind)
            #创建items对象
            item = MovieproItem()
            item['name'] = name
            item['kind'] = kind
            #问题：如何将剩下的电影详情数据存储到item对象（meta）
            #需要对url发起请求，获取页面数据，进行指定数据解析
            #meta参数只可以赋值一个字典（将item对象先封装到字典）
            yield scrapy.Request(url=url,callback=self.parseBySecondPage,meta={'item':item})