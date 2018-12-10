# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

#自定义一个下载中间件的类，在类中事先process_request（处理中间价拦截到的请求）方法
class MyProxy(object):
    def process_request(self,request,spider):
        #请求ip的更换
        request.meta['proxy'] = "https://178.128.90.1:8080"

