import re
import requests
from bs4 import BeautifulSoup
# import urllib.request


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
    def get_page_content(url):
        return requests.get(url)

    @staticmethod
    def remove_tags(text):
        """
        removes the <tags> from the given text
        """
        tag_re = re.compile(r'<[^>]+>')
        return tag_re.sub('', text)


class HinduScraper(Scraper):
    """
    inherits from Scraper class and contains
    functinalities to extracts editorials from hindu newspaper
    """

    def __init__(self, urls):
        super().__init__(urls)
        self.input_args = self.get_input_arguments()

    @staticmethod
    def get_input_arguments():
        print("\n Welcome to Hindu Editorial scraper \n")
        while True:
            user_input = input("latest(l) | specific(s)\n:>")
            if user_input in ["l", "s", "latest", "specific"]:
                return user_input
            else:
                print("Invalid argument")

    def get_editorial_links(self):
        if 'hindu' in self.urls.keys():
            response = self.get_page_content(self.urls['hindu'])
            page_content = response.content
            soup = BeautifulSoup(page_content, "lxml")
            links = soup.findAll("a")
            # editorial_links stores all the opinion/editorial links
            editorial_links = []
            for link in links:
                try:
                    if 'opinion/editorial' in link.get('href'):
                        s = link.get('href')
                        if s.endswith(".ece"):
                            editorial_links.append(s)
                # print(type(link.get('href')))
                except Exception:
                    pass

    def get_latest_editorial(self):
        if self.input_args in ["latest", "l"]:
            editorial_count = int(input("how many editorials you want to read\n:>"))
            print("---------------------------------------")
            i = 0
            editorial_links = self.get_editorial_links()
            print(editorial_links)
            while editorial_count > 0:
                response = requests.get(editorial_links[i] + '?homepage=true')
                # print(editorial_links[i])
                page2 = response.content
                soup = BeautifulSoup(page2, "lxml")
                content = soup.findAll("p")
                # print(type(content[0]))
                number_of_paragraphs = len(content)
                number_of_paragraphs -= 3
                print("Editorial " + str(i + 1) + "\n")
                for n in range(number_of_paragraphs):
                    print(self.remove_tags(str(content[n])))
                print("---------------------------------------")
                i += 1
                editorial_count -= 1

    def get_specific_editorial(self):
        if self.input_args in ["specific", "s"]:
            editorial_number = int(input("Which editorial do you want to read\n:>"))
            editorial_links = self.get_editorial_links()
            if editorial_number > 0:
                response = requests.get(
                    editorial_links[editorial_number - 1] + '?homepage=true')
                page2 = response.content
                soup = BeautifulSoup(page2, "lxml")
                content = soup.findAll("p")
                number_of_paragraphs = len(content)
                number_of_paragraphs -= 3
                print("----------------------------")
                for n in range(number_of_paragraphs):
                    print(self.remove_tags(str(content[n])))
                print("----------------------------")

    def read_editorials(self):
        if self.input_args in ["latest", "l"]:
            self.get_latest_editorial()
        if self.input_args in ["specific", "s"]:
            self.get_specific_editorial()


if __name__ == "__main__":
    urls = {
        'hindu': "http://www.thehindu.com/opinion/editorial/",
    }
    scraper = HinduScraper(urls)
    scraper.read_editorials()
