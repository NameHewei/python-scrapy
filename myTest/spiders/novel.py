# -*- coding: utf-8 -*-
import scrapy

# 引入自定义的items
from myTest.items import NovelItem

# 继承scrapy.Spider
class NovelSpider(scrapy.Spider):
    # 爬虫名
    name = 'novel_spider'
    # 允许的域名
    allowed_domains = ['http://www.danmeila.com']
    # 入口url 扔到调度器里面去
    start_urls = ['http://www.danmeila.com/chapter/20180406/29649.html']

    def parse(self, response):
        movieList = response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/div/div/ul/li')
        novelContent = NovelItem()
        for item in movieList:
            u = 'http://www.danmeila.com' + item.xpath('.//a/@href').extract_first()
            # print(u)
            # novelContent['title'] = 'http://www.danmeila.com' + item.xpath('.//a/@href').extract_first()    

            # yield novelContent
            # self.start_urls.append('http://www.danmeila.com' + item.xpath('.//a/@href').extract_first())
            yield scrapy.Request(u, callback = self.content_a, meta= novelContent)
            # 放到管道里否则 pipeline获取不到


    def content_a(self, response):
        print(11)
        novelContent = response.meta
        
        novelContent['title'] = response.xpath('//*[@id="J_article"]/div[1]/h1/text()').extract_first()    
        # novelContent['content'] = response.xpath('//*[@id="J_article_con"]/text()').extract_first()

        yield novelContent