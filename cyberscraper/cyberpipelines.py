from scrapy.exceptions import DropItem
import json

class DedupePipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem('Duplicate URL found: {}'.format(item))
        else:
            self.urls_seen.add(item['url'])
            return item

class CountCybers(object):

    def __init__(self):
        self.cybers = 0
        self.titles = []
        self.urls = []

    def process_item(self, item, spider):
        self.cybers += item['cybers']
        #print("{} cybers so far!".format(self.cybers))
        self.titles.append(item['title'])
        self.urls.append(item['url'])

    def close_spider(self, spider):
        # add the cybers to the DB
        with open('cybers.json', 'wb') as f:
            obj = {
                    'cybers': self.cybers,
                    'titles': self.titles,
                    'urls': self.urls
            }
            f.write(json.dumps(obj))
