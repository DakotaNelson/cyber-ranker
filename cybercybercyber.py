import scrapy
from scrapy.crawler import CrawlerProcess
import sys

from cyberscraper.cyberspider import CyberSpider

startUrl = sys.argv[1]

process = CrawlerProcess({
    'ITEM_PIPELINES': {
        'cyberscraper.cyberpipelines.DedupePipeline': 100,
        'cyberscraper.cyberpipelines.CountCybers': 900
    },
    #LOG_FILE =
    'TELNETCONSOLE_ENABLED': False,
    'COOKIES_ENABLED': False,
    'USER_AGENT': "Scrapy/CyberRank.net",
    'CLOSESPIDER_PAGECOUNT': 1000,
    'CLOSESPIDER_TIMEOUT': 3600
})

process.crawl(CyberSpider, startUrl=startUrl)
process.start()

print("")
print("All done!")
