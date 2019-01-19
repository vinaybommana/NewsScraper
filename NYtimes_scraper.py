import requests
import sys
from typing import List

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    'api-key': "52b1c21e060348b2a11e41b24d08c891",
    'q': "science",
    'begin_date': "20181229",
    'end_date': "20181231",
}


def get_query() -> List:
    return sys.argv[1:]


def give_query_to_params() -> None:
    queries = get_query()
    if len(queries) == 1:
        params['q'] = queries[0]


def get_nytimes_doc_weburls(url: str, params: dict) -> List:
    """ Return NYTimes response --> doc --> web_urls """
    output = requests.get(url=url, params=params)
    response = output.json()['response']
    docs = response['docs']
    web_urls = []
    for doc in docs:
        web_urls.append(doc['web_url'])

    return web_urls
