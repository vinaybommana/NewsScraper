# from datetime import datetime, date, time
from typing import List
# from bs4 import BeautifulSoup
# import calendar
import requests
import sys

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    'api-key': "52b1c21e060348b2a11e41b24d08c891",
    'q': "science",
    'begin_date': "20181229",
    'end_date': "20181231",
}


class NYScraper(object):
    pass


class ClassicNYScraper(object):
    """ NYScraper primitive class. """

    def __init__(self, url: str, params: dict) -> None:
        self.url = url
        self.params = params

    def get_nytimes_doc_weburls(self) -> List:
        """ Return NYTimes response --> doc --> web_urls """
        output = requests.get(url=self.url, params=self.params)
        response = output.json()['response']
        docs = response['docs']
        web_urls = []
        for doc in docs:
            web_urls.append(doc['web_url'])

        return web_urls


def get_query() -> List:
    """ return command line argument list. """
    return sys.argv[1:]


def give_query_to_params() -> None:
    """ add query from command line argument to params. """
    queries = get_query()
    if len(queries) == 1:
        params['q'] = queries[0]
    # print(params)


def give_content_from_link(url: str) -> str:
    """ Read the content from the link given.
        Requires Beautiful Soup Library.
    """
    pass


print(params)
give_query_to_params()
print(params)
