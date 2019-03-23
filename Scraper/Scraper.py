import re
import requests
from bs4 import BeautifulSoup
from typing import List


class Scraper(object):
    """
    Extract editorials from the list
    of news papers
    :input: urls is a dictionary,
        urls = {
            'hindu': "http://www.thehindu.com/opinion/editorial/",
        }
    """

    def __init__(self, urls):
        self.urls = urls

    @staticmethod
    def get_page_content(url, params=None):
        return requests.get(url, params)

    @staticmethod
    def remove_tags(text):
        """
        removes the <tags> from the given text
        """
        tag_re = re.compile(r"<[^>]+>")
        return tag_re.sub("", text)

    def give_content_from_link(self, url: str) -> List:
        """ Read the content from the link given.
            Requires Beautiful Soup Library.
        """
        response = self.get_page_content(url)
        page_content = response.content
        soup = BeautifulSoup(page_content, "lxml")
        content = soup.findAll("p")

        return content
