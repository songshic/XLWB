# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from  xinlangweibo.items import XlweiboItem
import pymongo


class XlweiboPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,XlweiboItem):
            if item.get('created_at'):
                item['created_at']=item['created_at'].strip()
                item['created_at']=self.parse_time(item['created_at'])
        return item

    def parse_time(self, datatime):
        datatime = time.strptime(datatime,'%a %b %d %H:%M:%S %z %Y')
        datatime = time.strftime('%Y-%m-%d %H:%M:%S',datatime)
        return datatime

class MongoPipeline():
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url=mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client =pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        self.db[item.table_name].update({'screen_name':item.get('screen_name')},{'$set':dict(item)},True)
        return item