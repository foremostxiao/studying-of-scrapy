# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']
    def parse(self, response):
        #建议大家使用xpath进行指定内容的解析（框架集成了xpath解析的接口）
        # 段子的内容和作者
        div_list = response.xpath('//div[@id="content-left"]/div')
        #存储解析到的页面数据
        data_list = []
        for div in div_list:
            #xpath解析到的指定内容被存储到了Selector对象
            #extract()该方法可以将Selector对象中存储的数据值拿到
            #author = div.xpath('./div/a[2]/h2/text()').extract()[0]
            #extract_first()  ==   extract()[0]
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            dict = {
                'author':author,
                'content':content
            }
            data_list.append(dict)
        return data_list