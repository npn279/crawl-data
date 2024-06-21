import requests
import urllib3
import ssl
from bs4 import BeautifulSoup


class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

url = 'https://example.com/'
response = get_legacy_session().get(url)

soup = BeautifulSoup(response.text, 'html.parser') 
a_tags = soup.select('div.list-news a')
links = [a['href'] for a in a_tags]
links = list(set(links))
for link in links:
    print(link)