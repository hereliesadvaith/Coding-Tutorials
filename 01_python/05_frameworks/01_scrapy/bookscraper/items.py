# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def serialize_price(value):
    """
    To serialize price field
    """
    return value


class BookscraperItem(scrapy.Item):
    """
    define the fields for your item here like
    """
    name = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field(serializer=serialize_price)
    availability = scrapy.Field()
