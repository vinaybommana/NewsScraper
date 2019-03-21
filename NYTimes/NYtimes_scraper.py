# from bs4 import BeautifulSoup
# from datetime import datetime, date, time
# import calendar
from typing import List
import json
import os
import sys

working_dir = os.path.dirname(os.path.abspath(__file__))
# print(working_dir)

sys.path.append(os.path.abspath(os.path.join("..", "utils")))
sys.path.append(os.path.abspath(os.path.join("..", "Scraper")))

# print(sys.path)

import utils
from Scraper import Scraper


b_date, e_date = utils.form_dates("week")
# print(b_date, e_date)

# load configs
working_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join("../configs.json")) as w:
    config_data = json.load(w)

# globals
api_key = config_data["ny-api-key"]
ny_url = config_data["ny-ar-url"]


class ClassicNYScraper(Scraper):
    """ NYScraper primitive class.

    Usage:
        ClassicNYScraper(urls, params)
    """

    def __init__(self, urls: str, params: dict) -> None:
        super().__init__(urls)
        self.url = ""
        if "nytimes" in self.urls.keys():
            self.url = self.urls["nytimes"]
        self.params = params
        self.give_query_to_params()
        # print(self.params)

    def get_nytimes_doc_weburls(self) -> List:
        """ Return NYTimes response --> doc --> web_urls """
        output = self.get_page_content(url=self.url, params=self.params)
        response = output.json()["response"]
        docs = response["docs"]
        web_urls = []
        for doc in docs:
            web_urls.append(doc["web_url"])

        return web_urls

    @staticmethod
    def get_query() -> List:
        """ return command line argument list. """
        if len(sys.argv) <= 1:
            print("Please provide valid query arguments.")
            sys.exit(0)
        return sys.argv[1:]

    def give_query_to_params(self) -> None:
        """ add query from command line argument to params. """
        queries = self.get_query()
        if len(queries) == 1:
            self.params["q"] = queries[0]


def give_content_from_link(url: str) -> str:
    """ Read the content from the link given.
        Requires Beautiful Soup Library.
    """
    pass


urls = {"nytimes": ny_url}
params = {"api-key": api_key, "q": "", "begin_date": b_date, "end_date": e_date}

scraper = ClassicNYScraper(urls, params)
# print(scraper.get_nytimes_doc_weburls())
