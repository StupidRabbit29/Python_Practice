# -*- coding: utf-8 -*-

# Define here the models for your scraped items

# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # 要爬的内容
    name = scrapy.Field()
    loc1 = scrapy.Field()
    loc2 = scrapy.Field()
    loc3 = scrapy.Field()
    housetype = scrapy.Field()
    avgprice = scrapy.Field()
    tolprice = scrapy.Field()
    area = scrapy.Field()
