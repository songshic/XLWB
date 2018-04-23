# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XlweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table_name = 'xlweibo'
    screen_name = scrapy.Field()
    text =  scrapy.Field()
    source = scrapy.Field()
    retweeted_status_text = scrapy.Field()
    created_at = scrapy.Field()
