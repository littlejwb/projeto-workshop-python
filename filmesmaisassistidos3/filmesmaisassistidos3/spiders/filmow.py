import scrapy


class FilmowSpider(scrapy.Spider):
    name = 'filmow'
    allowed_domains = ['filmow.com']
    start_urls = ['https://filmow.com/filmes-todos/?order=saw&filters=&apply=']

    def parse(self, response):
        for span in response.css('.wrapper'):
            filmes = span.css('.title::text').get()
            yield{
                'filmes' : filmes 
            }
        pass
