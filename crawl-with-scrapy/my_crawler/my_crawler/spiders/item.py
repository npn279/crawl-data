from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class MyCrawler(CrawlSpider):
    name = 'my_crawler'
    allowed_domains = ['tainguyenmoitruong.gov.vn']
    start_urls = ['https://tainguyenmoitruong.gov.vn/']
    rules = (
        Rule(LinkExtractor(allow=['/tin-tuc-su-kien/']), follow=True, callback='parse'),
    )

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')

        title = soup.select_one('h1.title')
        if title:
            title = title.get_text(strip=True)
        else:
            title = ""

        yield {
            'url': response.url,
            'title': title,
        }
