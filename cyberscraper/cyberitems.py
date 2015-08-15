import scrapy

class CyberRank(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    cybers = scrapy.Field()
