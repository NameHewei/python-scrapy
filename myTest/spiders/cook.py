# -*- coding: utf-8 -*-
import scrapy

# 引入自定义的items
from myTest.items import MytestItem

# 继承scrapy.Spider
class CookSpider(scrapy.Spider):
    # 爬虫名
    name = 'cook_spider'
    # 允许的域名
    allowed_domains = ['www.xiachufang.com']
    # 入口url 扔到调度器里面去
    start_urls = ['http://www.xiachufang.com/category/40077/']

    def parse(self, response):
        movieList = response.xpath('//html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[2]/ul/li')
        for item in movieList:
            testItem = MytestItem()
            testItem['name'] = item.xpath('normalize-space(.//div/div/p[1]/a/text())').extract_first()
            testItem['imgUrl'] = item.xpath('.//div/a/div/img/@data-src').extract_first()

            
            # 放到管道里否则 pipeline获取不到
            yield testItem
