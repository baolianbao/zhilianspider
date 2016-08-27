# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
from zhilian.items import JobItem


class AJobSpider(scrapy.Spider):
    name = "ajob"
    allowed_domains = ["zhaopin.com"]
    start_urls = (
        'http://jobs.zhaopin.com/zhengzhou_re2401/',
    )

    def parse(self, response):
        for job in response.xpath('//*[contains(@class,"details_container")]'):
            item = JobItem()
            # print job.xpath('//*/span[@class="salary"]/text()').extract()
            item["title"] = job.xpath('//*/span[@class="post"]/a/text()').extract()
            item["company"] = job.xpath('//*/span[@class="company_name"]/a/text()').extract()
            item["salary"] = job.xpath('//*/span[@class="salary"]/text()').extract()

            yield item