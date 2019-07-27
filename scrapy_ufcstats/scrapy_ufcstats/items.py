# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyUfcstatsItem(scrapy.Item):
    # define the fields for your item here like:
    fighter_1 = scrapy.Field()
    fighter_1_nn = scrapy.Field()
    fighter_2 = scrapy.Field()
    fighter_2_nn = scrapy.Field()
    winner = scrapy.Field()
    date = scrapy.Field()