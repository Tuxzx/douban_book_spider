# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from douban.items import DoubanItem
import sys

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/']

    def parse(self, response):
        print('parse')
        links = response.xpath("//*[@class = 'tagCol']/descendant::a/@href").extract()
        # print(links)
        for herf in links:
            for pageNum in range(0,180,20):
                listpageUrl = response.urljoin(herf+'/?start='+str(int(pageNum)) + "&type=T")
                # print(listpageUrl)
                # sys.exit()
                yield scrapy.Request(listpageUrl, callback=self.parse_tag_per_page)

    def parse_tag_per_page(self, response):
        print('parse_tag_per_page')
        links = response.xpath("//ul[@class = 'subject-list']/descendant::a[@class = 'nbg']/@href").extract()
        for book in links:
            yield scrapy.Request(book, callback=self.parse_book)

    def parse_book(self, response):
        print('parse_tag_per_page')
        item = DoubanItem()
        sel = Selector(response)
        e = sel.xpath("//div[@id='wrapper']")
        item['name'] = e.xpath("./descendant::h1/descendant::span/text()").extract()
        item['author'] = e.xpath("//span[contains(./text(), '作者')]/following::text()[2]").extract()
        item['press'] = e.xpath("//*[@id='info']/span[contains(./text(), '出版社:')]/following::text()[1]").extract()
        item['pressdate'] = e.xpath("//*[@id='info']/span[contains(./text(), '出版年:')]/following::text()[1]").extract()
        item['pagenum'] = e.xpath("//*[@id='info']/span[contains(./text(), '页数:')]/following::text()[1]").extract()
        item['price'] = e.xpath("//*[@id='info']/span[contains(./text(), '定价:')]/following::text()[1]").extract()
        item['isbn'] = e.xpath("//*[@id='info']/span[contains(./text(), 'ISBN:')]/following::text()[1]").extract()
        item['bookinfo'] = e.xpath("//div[contains(@class, 'intro')]/p/text()").extract()
        item['tag'] = response.xpath("//*[@id = 'db-tags-section']/descendant::a/text()").extract()
         
                
        print('parse_book {}'.format(item))
        return item
        