import scrapy

class SureshSpider(scrapy.Spider):
    name = 'suresh'
    start_urls = ['https://vinepair.com/articles/best-wines-2019/']
    
    def parse(self, response):
        for title in response.css('#post-74227 > div > h3 > a'):
            yield{
                'title':title.css('::text').get()
            }
            
        
#post-74227 > div > h3 > a