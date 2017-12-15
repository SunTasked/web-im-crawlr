import sys
sys.path.insert(0, './crawler/spiders/py-scripts')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from mongo_access import insert_image
from utils import valid_ext


class MySpider(CrawlSpider):
    name = 'image_zog'
    allowed_domains = ['imagezog.com']
    start_urls = ['http://imagezog.com/']

    
    custom_settings = {
        "AUTOTHROTTLE_ENABLED":True,
        "AUTOTHROTTLE_START_DELAY":0.1,
        "AUTOTHROTTLE_MAX_DELAY":0.3,
        "AUTOTHROTTLE_TARGET_CONCURRENCY":10
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = Selector(response)
        # this xpath selector will only select the full sized images and ignore the mini.
        imgurls = hxs.xpath("//div/p[contains(@class, 'photo')]/img/@src").extract()
        imgurls = list(map(lambda x: x.split('?')[0], imgurls))

        for imgurl in imgurls : 
            if not(valid_ext(imgurl)):
                continue
            image_obj = {
                "image_url" : imgurl,
                "webpage_url" : response.url
            }
            insert_image(image_obj)
