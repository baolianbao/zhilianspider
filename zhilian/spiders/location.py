# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import ZhengzhouItem


class LocationSpider(scrapy.Spider):
    name = "location"
    allowed_domains = ["zhaopin.com"]
    start_urls = (
        'http://jobs.zhaopin.com/zhengzhou_re2194',
        'http://jobs.zhaopin.com/zhengzhou_re2195',
        'http://jobs.zhaopin.com/zhengzhou_re2196',
        'http://jobs.zhaopin.com/zhengzhou_re2197',
        'http://jobs.zhaopin.com/zhengzhou_re2198',
        'http://jobs.zhaopin.com/zhengzhou_re2199',
        'http://jobs.zhaopin.com/zhengzhou_re2203',
        'http://jobs.zhaopin.com/zhengzhou_re2204',
        'http://jobs.zhaopin.com/zhengzhou_re2205',
        'http://jobs.zhaopin.com/zhengzhou_re2399',
        'http://jobs.zhaopin.com/zhengzhou_re2400',
        'http://jobs.zhaopin.com/zhengzhou_re2401',
        'http://jobs.zhaopin.com/zhengzhou_re2402',
        'http://jobs.zhaopin.com/zhengzhou_re2403',
        'http://jobs.zhaopin.com/zhengzhou_re2444',
        'http://jobs.zhaopin.com/zhengzhou_re2445',
    )

    def parse(self, response):
        item = ZhengzhouItem()
        item['region'] = response.xpath('//*[@id="search_city"]/div/a[@class="currentlimit"]/text()').extract()
        item["location_urls"] = response.xpath('//*[@id="search_city_main"]/div[@class="listcon"]/a/@href').extract()
        return item
        # self.log("Region: %s" %  response.xpath('//*[@id="search_city"]/div/a[@class="currentlimit"]/text()').extract())
        # for url in  response.xpath('//*[@id="search_city_main"]/div[@class="listcon"]/a/@href').extract():
        #     self.log("Locations URLs %s " % url)
