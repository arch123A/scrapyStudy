# -*- coding: utf-8 -*-
from datetime import datetime
from urllib.parse import urljoin

import scrapy


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        # 提取当前页
        # 先分组，再提取
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item = dict(
                title=tr.xpath(".//a/text()").extract_first(),
                category=tr.xpath(".//td[2]/text()").extract_first(),
                need_count=tr.xpath(".//td[3]/text()").extract_first(),
                address=tr.xpath(".//td[4]/text()").extract_first(),
                data=datetime.strptime(tr.xpath(".//td[5]/text()").extract_first(), '%Y-%m-%d'),
            )
            print(item)
            yield item
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # 判断是否是下一页
        if next_url != "javascript:;":
            # next_url= urljoin(response.url,next_url)
            # yield scrapy.Request(next_url,callback=self.parse)

            # 利用follow方法
            yield response.follow(next_url)
