# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # 要爬的内容
    university = scrapy.Field()
    classnum = scrapy.Field()


