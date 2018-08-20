# -*- coding: utf-8 -*-
import scrapy

# 引入自定义的items
from myTest.items import NovelItem

# 继承scrapy.Spider
class NovelSpider(scrapy.Spider):
    # 爬虫名
    name = 'novel_spider'
    # 允许的域名
    allowed_domains = ['http://hao123.zongheng.com']
    # 入口url 扔到调度器里面去
    start_urls = ['http://hao123.zongheng.com/book/1/189169.html']

    def parse(self, response):
        movieList = response.xpath('//*[@id="ct"]/div/div[2]/div/div[2]/div/div[6]/div[2]/ul/li')
        for item in movieList:
            testItem = NovelItem()
            testItem['title'] = item.xpath('.//a/@title').extract_first()
            
            # 放到管道里否则 pipeline获取不到
            yield testItem
