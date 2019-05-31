# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class CreatorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    creator_text = 	scrapy.Field(
    	input_processor= MapCompose(remove_tags),
    	output_processor= TakeFirst()
    	)