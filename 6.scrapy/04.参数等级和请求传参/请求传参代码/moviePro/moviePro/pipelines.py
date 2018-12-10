# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MovieproPipeline(object):
    fp = None
    def open_spider(self,spider):
        self.fp = open('movie.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        detail = item['name']+':'+item['kind']+':'+item['actor']+':'+item['language']+':'+item['longTime']+'\n\n\n'
        self.fp.write(detail)
        return item
    def close_spider(self,spider):
        self.fp.close()
