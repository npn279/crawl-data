# Installation
```
pip install scrapy
```

# Run
## 1. Start project
```
scrapy startproject <project_name>
cd <project_name>
```

## 2. Code parse funtion
Inside *<project_name>/<project_name>/spiders*, create *item.py*

```python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class MyCrawler(CrawlSpider):
    name = 'my_crawler'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/abc.html']
    rules = (
        Rule(LinkExtractor(allow=['/news/']), follow=True, callback='parse'),
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
```

### Start scrawler
To crawl data, use

```
scrapy crawl <project_name> -o data.jsonl
```

