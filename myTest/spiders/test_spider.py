# -*- coding: utf-8 -*-
import scrapy

# 引入自定义的items
from myTest.items import MytestItem

# 继承scrapy.Spider
class TestSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'test_spider'
    # 允许的域名        
    allowed_domains = ['movie.douban.com']
    # 入口url 扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movieList = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for item in movieList:
            testItem = MytestItem()
            testItem['movieName'] = item.xpath('.//div/div[2]/div[1]/a/span[1]/text()').extract_first()
            testItem['movieRate'] = item.xpath('.//div/div[2]/div[2]/div/span[2]/text()').extract_first()
            
            # 放到管道里否则 pipeline获取不到
            yield testItem

        nextLink = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0] 
            yield scrapy.Request('https://movie.douban.com/top250' + nextLink, callback = self.parse)
