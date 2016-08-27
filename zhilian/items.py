# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ZhengzhouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Company Name
    # >>> response.xpath('//*/ul[@class="search_list"]/li/div[4]/span[@class="post"]/a/text()').extract()
    # region = Field()
    region = Field()
    location_urls = Field()


class JobItem(Item):
    title = Field()
    company = Field()
    salary = Field()
    location = Field()
    