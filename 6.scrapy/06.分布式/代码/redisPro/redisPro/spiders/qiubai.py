# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redisPro.items import RedisproItem
from scrapy_redis.spiders import RedisCrawlSpider
from redisPro.items import RedisproItem

class QiubaiSpider(RedisCrawlSpider):
    name = 'qiubai'
    #allowed_domains = ['https://www.qiushibaike.com/pic/']
    #start_urls = ['https://www.qiushibaike.com/pic/']

    #调度器队列的名称
    redis_key = 'qiubaispider'  #表示跟start_urls含义是一样

    #【注意】近期糗事百科更新了糗图板块的反爬机制，更新后该板块的页码链接/pic/page/2/s=5135066，末尾的数字每次页面刷新都会变化，因此正则不可写为/pic/page/\d+/s=5135066而应该修改成/pic/page/\d+
    link = LinkExtractor(allow=r'/pic/page/\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       #将图片的url进行解析

        div_list = response.xpath('//*[@id="content-left"]/div')
        for div in div_list:
            img_url = div.xpath('./div[@class="thumb"]/a/img/@src').extract_first()
            item = RedisproItem()
            item['img_url'] = img_url

            yield item
