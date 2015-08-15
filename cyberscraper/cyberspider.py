# Scrapes websites, ranks how frequently they use the word "cyber" (including as a prefix to other words: cybersecurity, cybercrime, etc.)

# inspired by: http://www.hackerhalted.com/2015/home/
# look at all that cyber!

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from urlparse import urlparse
import sys
import re

from cyberitems import CyberRank

class CyberSpider(scrapy.spiders.CrawlSpider):
    name = "cyberspider"
    download_delay = 2

    def __init__(self, startUrl):
        if type(startUrl) is not str:
            raise ValueError('startUrl must be a string representing a valid URL')


        self.start_urls = [startUrl]
        self.allowed_domains = [urlparse(startUrl).netloc]

        self.logger.info("Crawling {} starting at {}".format(self.start_urls[0], self.allowed_domains[0]))

        self.rules = (
            # Extract all links that point to the same domain.
            Rule(LinkExtractor(allow=(self.allowed_domains[0])), callback='findCybers', follow=True),
        )

        super(CyberSpider, self).__init__(startUrl)

    def findCybers(self, response):
        allText = ''.join(response.xpath("//body//text()").extract()).strip()
        cybers = re.findall('cyber', allText, re.IGNORECASE)
        self.logger.info("Found {} cybers!".format(len(cybers)))

        rank = CyberRank()
        rank['url'] = response.url
        rank['title'] = response.xpath('//title/text()').extract()[0]
        rank['cybers'] = len(cybers)
        return rank
