# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AccItem(scrapy.Item):
    # define the fields for your item here like:
    # 字典的key
    title = scrapy.Field()
    text = scrapy.Field()
