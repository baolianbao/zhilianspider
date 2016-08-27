# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
from zhilian.items import JobItem


class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["zhaopin.com"]
    start_urls = (
        'http://jobs.zhaopin.com/zhengzhou_re2401/',
    )
    # start_urls = [i.strip() for i in open('/zz_areas.txt').readlines()]

    def parse(self, response):
        # Get next URLs and yield Requests    
        next_selector = response.xpath('//*[@class="search_page_next"]/a/@href')  
        for url in next_selector.extract():
            print response.url
            yield Request(urlparse.urljoin('http://jobs.zhaopin.com', url),                      
                callback=self.parse_item)        
                # yield Request(urlparse.urljoin(response.url, url),                      
                # callback=self.parse_item)

    def parse_item(self, response):
        for job in response.xpath('//*[@class="details_container"]').extract():
            item = JobItem()
            item["title"] = job.xpath('//*/span[@class="post"]/a/text()').extract()
            item["company"] = job.xpath('//*/span[@class="company_name"]/a/text()').extract()
            item["salary"] = job.xpath('//*/span[@class="salary"]/text()').extract()

            yield item
            

    def get_item(self, job):
        item = JobItem()
        item["title"] = job.xpath('//*/span[@class="post"]/a/text()').extract()
        item["company"] = job.xpath('//*/span[@class="company_name"]/a/text()').extract()
        item["salary"] = job.xpath('//*/span[@class="salary"]/a/text()').extract()

        return item