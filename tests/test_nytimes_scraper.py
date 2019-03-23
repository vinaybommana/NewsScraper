#! /usr/bin/python3
import os
import sys
import json
import unittest
import requests

working_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join("../configs.json")) as w:
    config_data = json.load(w)

sys.path.append(os.path.abspath(os.path.join("..", "NYTimes")))
sys.path.append(os.path.abspath(os.path.join("..", "utils")))

import NYtimes_scraper
import utils

b_date, e_date = utils.form_dates(range="week")


class TestNYScraper(unittest.TestCase):

    def setUp(self):
        self.query = "science"
        self.api_key = config_data["ny-api-key"]
        self.ny_url = config_data["ny-ar-url"]
        self.urls = {"nytimes": self.ny_url}
        self.params = {
            "api-key": self.api_key,
            "q": self.query,
            "begin_date": b_date,
            "end_date": e_date
        }
        self.scraper = NYtimes_scraper.ClassicNYScraper(self.urls, self.params)
        self.weburls = self.scraper.get_nytimes_doc_weburls()

    def test_nytimes_doc_weburls(self):
        self.assertIsInstance(self.weburls, list)

    def test_status_weburls(self):
        self.assertEqual(requests.get(self.weburls[0]).status_code, 200)

    def test_give_content_from_link(self):
        self.assertIsInstance(self.scraper.give_content_from_link(self.weburls[0]), str)


if __name__ == "__main__":
    unittest.main()
