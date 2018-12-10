# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiproPipeline(object):
    fp = None
    #整个爬虫过程中，该方法只会在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./qiubai_pipe2.txt', 'w', encoding='utf-8')
    #该方法就可以接受爬虫文件中提交过来的item对象，并且对item对象中存储的页面数据进行持久化存储
    #参数：item表示的就是接收到的item对象
    #每当爬虫文件向管道提交一次item，则该方法就会被执行一次
    def process_item(self, item, spider):
        #print('process_item 被调用！！！')
        #取出item对象中存储的数据值
        author = item['author']
        content = item['content']

        #持久化存储
        self.fp.write(author+":"+content+'\n\n\n')
        return item
    #该方法只会在爬虫结束的时候被调用一次
    def close_spider(self,spider):
        print('爬虫结束')
        self.fp.close()