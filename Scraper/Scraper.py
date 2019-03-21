import re
import requests


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
