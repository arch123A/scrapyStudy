# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field() #编号
    title = scrapy.Field()
    status = scrapy.Field()
    href = scrapy.Field()  # 链接
    name = scrapy.Field()  # 发贴人
    date = scrapy.Field()
    img = scrapy.Field()
    content = scrapy.Field()
    pass
