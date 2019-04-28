# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名?
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 爬到所有人的列表
        li_list = response.xpath("//div[@class='tea_con']/div/ul/li")  # .extract()提取文本

        for li in li_list:
            item = dict(name=li.xpath('.//h3/text()').extract_first(),
                        digest=li.xpath('.//p/text()').extract_first(),
                        image=li.xpath(".//div[@class='li_img']/img/@data-original").extract_first(),
                        )
            print(item)
