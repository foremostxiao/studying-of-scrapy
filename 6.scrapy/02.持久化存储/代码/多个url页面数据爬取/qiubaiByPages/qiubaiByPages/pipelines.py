# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaibypagesPipeline(object):
    fp = None
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(item['author']+":"+item['content'])
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束')