# -*- coding: utf-8 -*-
import scrapy
from ..items import MeizituItem
from scrapy import Request
class MztspdSpider(scrapy.Spider):
    name = 'mztspd'
    allowed_domains = ['http://www.meizitu.com']
    start_urls = ['http://www.meizitu.com/a/5546.html']
    url = ''

    def parse(self, response):
        item = MeizituItem()
        # info = response.xpath('//div[id="picture"]')
        # item['name'] = response.xpath('//div[@id="picture"]/p/img/@alt').extract()
        item['image_urls'] = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        yield item

        i = 5546
        while i > 5200:
            next_page = str(i) + '.html'
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse,dont_filter=True)
            i = i - 1

        # if next_page is not None:
        #     next_page = next_page[0]
        #     print(next_page)
        #     yield Request(next_page, callback=self.parse,dont_filter=True)
        #


        # for name in names:
        #     item['name'] = name
        #
        #
        # for img in imgs:
        #     item['url'] = img
        #     yield item
        # for info in response.xpath('//div[id="picture"]/p'):
        #     names = info.xpath('/img/@alt').extract()
        #     img = info.xpath('/img/@src').extract()
        #     item['name'] = name
        #     item['url'] = img
        #     yield item
        # names = response.xpath('//div[@id="picture"]/p/img/@alt').extract()
        # imgs = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        # for name in names:
        #     for img in imgs:
        #         item['name'] = name
        #         item['url'] = img
        #     yield item
