# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy

from dongguan.items import DongguanItem


class DgSpider(scrapy.Spider):
    name = 'dg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/reply?page=0']

    def parse(self, response):
        # print(response)
        tr_list=response.xpath('//table[2]/tr')
        # /td[3]/a[1]/text()
        for tr in tr_list:
            item=DongguanItem()
            item['num']=tr.xpath('./td[1]/text()').extract_first()
            item['title']=tr.xpath('./td[3]/a[1]/text()').extract_first()
            item['href']=tr.xpath('./td[3]/a[1]/@href').extract_first()
            item['status']=tr.xpath('./td[4]/span/text()').extract_first()
            item['name']=tr.xpath('./td[5]/text()').extract_first()
            item['date']=tr.xpath('./td[6]/text()').extract_first()
            yield scrapy.Request(item['href'], callback=self.detail_parse,meta={'item':item})


        next_url = response.xpath(r'//div[@class="pagination"]//a[text()=">"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url,callback=self.parse)


    def detail_parse(self,response):
        item=response.meta['item']
        content=response.xpath("//div[@class='wzy1']//table[2]//td[@class='txt16_3'][1]/text()").extract()

        item['content']=content
        img=response.xpath("//div[@class='wzy1']//table[2]//td[@class='txt16_3'][1]//img/@src").extract_first()
        item['img']=urljoin(response.url,img) if img else None
        print(img)
        yield item

