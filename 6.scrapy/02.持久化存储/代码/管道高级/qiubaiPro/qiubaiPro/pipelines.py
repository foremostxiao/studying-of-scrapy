# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class QiubaiproPipeline(object):
    conn = None
    def open_spider(self,spider):
        print('开始爬虫')
        self.conn = redis.Redis(host='127.0.0.1',port=6379)
    def process_item(self, item, spider):
        dict = {
            'author':item['author'],
            'content':item['content']
        }
        self.conn.lpush('data', dict)
        return item

#实现将数据值存储到本地磁盘中
class QiubaiByFiles(object):
    def process_item(self,item,spider):
        print("数据已经写入指定的磁盘文件中")
        return item

#实现将数据值存储到mysql数据库中
class QiubaiByMysql(object):
    def process_item(self,item,spider):
        print('数据已经写入到mysql数据库中')
        return item
