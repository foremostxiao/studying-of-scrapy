# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class QiubaiproPipeline(object):

    conn = None
    cursor = None
    def open_spider(self,spider):
        print('开始爬虫')
        #链接数据库
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123',db='qiubai')
    #编写向数据库中存储数据的相关代码
    def process_item(self, item, spider):
        #1.链接数据库
        #2.执行sql语句
        sql = 'insert into qiubai values("%s","%s")'%(item['author'],item['content'])
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        #3.提交事务

        return item
    def close_spider(self,spider):
        print('爬虫结束')
        self.cursor.close()
        self.conn.close()
