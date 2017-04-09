# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy_djangoitem import DjangoItem
from myapp.models import ExampleDotCom

# class ExampleBotItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()
#     pass
class ExampleDotComItem(DjangoItem):
    django_model = ExampleDotCom