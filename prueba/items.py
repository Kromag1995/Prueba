# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Divisa(scrapy.Item):
    descripcion = scrapy.Field()
    ultimo = scrapy.Field()
    anterior = scrapy.Field()
    variacion = scrapy.Field()
    fecha = scrapy.Field()
    pass
