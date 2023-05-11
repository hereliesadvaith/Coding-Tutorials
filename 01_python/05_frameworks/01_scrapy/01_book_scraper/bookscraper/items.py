# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# def serialize_description(description):
#     # you can clean the data
#     pass


class BookItem(scrapy.Item):
    name = scrapy.Field()
    # to use serializer
    # description = scrapy.Field(serializer=serialize_description)
    description = scrapy.Field()
    availability = scrapy.Field()
