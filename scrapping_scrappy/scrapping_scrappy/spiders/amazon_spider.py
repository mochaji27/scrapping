import scrapy
from pathlib import Path
from datetime import datetime

class Product(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    search = 'iphone 14 pro'
    base_url = 'http://www.amazon.com'

    allowed_domains = ['amazon.com']

    start_urls  = [
            f'{base_url}/s?k={search}'
        ]
        

    def parse(self, response):
        list_item = response.xpath('//div[@class="sg-col-inner"]')[4:]
        #name = list_item.xpath('./span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get()
        #print(list_item)
        for item in list_item:
            name = item.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get()
            type = item.xpath('.//span[@class="a-color-information a-text-bold"]/text()').get()
            rating = item.xpath('.//span[@class="a-icon-alt"]/text()').get()
            review = item.xpath('.//span[@class="a-size-base s-underline-text"]/text()').get()
            product = Product(name = name, type = type, rating = rating)
            url_item = item.xpath('.//a[@class="a-link-normal s-no-outline"]/@href').get()
            full_url_item = f"{self.base_url}{url_item}"
            print(full_url_item)
            yield scrapy.Request(full_url_item, callback=self.parse_item_detail)
    
    def parse_item_detail(self, response):
        print(response)
        
    

                    



