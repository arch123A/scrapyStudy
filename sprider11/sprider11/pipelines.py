# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sprider11Pipeline(object):
    def proces_item(self, item, spider):
        # 管道是专门处理数据的
        print(0000000)
        return item

#
# class Sprider11Pipeline1(object):
#     def process_item(self, item, spider):
#         # 管道是专门处理数据的
#         print(11111)
#         return item