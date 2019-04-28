# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy


class GkSpider(scrapy.Spider):
    name = 'gk'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="ask-list-cp"]/li')
        for li in li_list:
            item = dict(
                title=li.xpath('.//div[@class="ask-list-detials"]/h2/a/text()').extract_first(),
                href=li.xpath('.//div[@class="ask-list-detials"]/h2/a/@href').extract_first(),
                summary=li.xpath('.//p[@class="ask-list-summary"]/text()').extract_first().strip(),
                focus_num=li.xpath('.//span[1]/text()').extract_first(),
                answer_num=li.xpath('.//p[@class="ask-answer-nums"]/span/text()').extract_first(),
                tag=li.xpath('.//p[@class="tags"]/a/text()').extract(),
            )
            yield scrapy.Request(
                item['href'],
                callback=self.detail_parse,
                meta={"item":item}
            )
        next_url=response.xpath('//a[text()="下一页"]/@href').extract_first()
        # print(next_url)
        if next_url is not None:
            yield response.follow(next_url,callback=self.parse)

    def detail_parse(self,response):
        item=response.meta['item']
        quest_content=response.xpath('//div[@id="questionDesc"]/p/text()').extract()

        div_list=response.xpath('//div[contains(@class,"answer gclear")]')

        for  div in div_list:
            answer_dict={}
            # TODO  username
            username=div.xpath(".//a[@class='answer-usr-name']/text()").extract_first()
            print(username)


        # other_answer=response.xpath('//div[@class="answer-txt answerTxt gbbcode-content"]/text()').extract()
        other_answer=response.xpath('//div[@class="answer gclear   ghide"]/div[2]/div[3]/p/text()').extract()
        item['content']=quest_content
        item['other_answer']=other_answer
        answer_num=response.xpath('//div[@class="answers-do"]/span/text()').extract_first()
        # print(answer_num)
        # print(other_answer)
        # print(quest_content)


        # print(other_answer)
        yield item


