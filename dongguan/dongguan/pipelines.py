# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

client=MongoClient()
collection=client['dongguan']['dg']
class DongguanPipeline(object):
    def process_item(self, item, spider):
        collection.insert_one(dict(item))
        return item
