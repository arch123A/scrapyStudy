# -*- coding: utf-8 -*-
import scrapy


class GkSpider(scrapy.Spider):
    name = 'gk'
    allowed_domains = ['guokr.com']
    start_urls = ['http://guokr.com/']

    def parse(self, response):
        pass
