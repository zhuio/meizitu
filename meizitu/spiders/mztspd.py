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
        item['image_urls'] = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        yield item

        i = 5546
        while i > 3000:
            next_page = str(i) + '.html'
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse,dont_filter=True)
            i = i - 1

