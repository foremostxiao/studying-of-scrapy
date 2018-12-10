# -*- coding: utf-8 -*-
import scrapy
from qiubaiByPages.items import QiubaibypagesItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']

    #设计一个通用的url模板
    url = 'https://www.qiushibaike.com/text/page/%d/'
    pageNum = 1

    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')

        for div in div_list:
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            #创建一个items对象，将解析到数据值存储到items对象中
            item = QiubaibypagesItem()
            item['author'] = author
            item['content'] = content

            #将item提交给管道
            yield item

        #请求的手动发送
        #13表示的是最后一页的页码
        if self.pageNum <= 13:
            print('爬取到了第%d页的页面数据'%self.pageNum)
            self.pageNum += 1
            new_url = format(self.url % self.pageNum)
            yield scrapy.Request(url=new_url,callback=self.parse)



