# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class DoubanPipeline(object):
    def __init__(self):
        csvfile =  open('booktest.csv', 'w', encoding='utf8', newline='')
        self.f = csv.writer(csvfile)

    def process_item(self, item, spider):
        itemlist = [((item['name'])[0]).replace('\n','').replace(' ',''),
         ((item['author'])[0]).replace('\n','').replace(' ',''),
          ((item['press'])[0]).replace('\n','').replace(' ',''),
           ((item['pressdate'])[0]).replace('\n','').replace(' ',''),
            ((item['pagenum'])[0]).replace('\n','').replace(' ',''),
             ((item['price'])[0]).replace('\n','').replace(' ',''),
              ((item['isbn'])[0]).replace('\n','').replace(' ',''),
               ((item['tag'])[0]).replace('\n','').replace(' ',''),
                ((item['bookinfo'])[0]).replace('\n','') ]
        self.f.writerow(itemlist)
        return item

    def close_spider(self, spider):
        pass
