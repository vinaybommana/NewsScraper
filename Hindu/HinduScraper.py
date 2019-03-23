from Scraper import Scraper
from bs4 import BeautifulSoup
import requests


class HinduScraper(Scraper):
    """
    inherits from Scraper class and contains
    functinalities to extracts editorials from hindu newspaper
    """

    def __init__(self, urls):
        super().__init__(urls)
        self.url = ""
        if "hindu" in self.urls.keys():
            self.url = self.urls["hindu"]
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
        response = self.get_page_content(self.url)
        page_content = response.content
        soup = BeautifulSoup(page_content, "lxml")
        links = soup.findAll("a")
        # editorial_links stores all the opinion/editorial links
        editorial_links = []
        for link in links:
            try:
                if "opinion/editorial" in link.get("href"):
                    s = link.get("href")
                    if s.endswith(".ece"):
                        editorial_links.append(s)
            # print(type(link.get('href')))
            except Exception:
                pass
        return editorial_links

    def get_latest_editorial(self):
        if self.input_args in ["latest", "l"]:
            editorial_count = int(input("how many editorials you want to read\n:>"))
            print("---------------------------------------")
            i = 0
            editorial_links = self.get_editorial_links()
            while editorial_count > 0:
                response = requests.get(editorial_links[i] + "?homepage=true")
                # print(editorial_links[i])
                page2 = response.content
                soup = BeautifulSoup(page2, "lxml")
                content = soup.findAll("p")
                # print(type(content[0]))
                number_of_paragraphs = len(content)
                # removing the last three tags
                number_of_paragraphs -= 3
                print("Editorial " + str(i + 1) + "\n")
                elements = []
                for n in range(number_of_paragraphs):
                    elements.append(self.remove_tags(str(content[n])))
                time = elements[len(elements) - 1]
                elements = [i for i in elements if not i.startswith("\n")]
                for item in elements:
                    print(item)
                print(time)
                print("---------------------------------------")
                i += 1
                editorial_count -= 1

    def get_specific_editorial(self):
        if self.input_args in ["specific", "s"]:
            editorial_number = int(input("Which editorial do you want to read\n:>"))
            editorial_links = self.get_editorial_links()
            if editorial_number > 0:
                response = requests.get(editorial_links[editorial_number - 1] + "?homepage=true")
                page2 = response.content
                soup = BeautifulSoup(page2, "lxml")
                content = soup.findAll("p")
                number_of_paragraphs = len(content)
                number_of_paragraphs -= 3
                print("----------------------------")
                elements = []
                for n in range(number_of_paragraphs):
                    elements.append(self.remove_tags(str(content[n])))
                time = elements[len(elements) - 1]
                elements = [i for i in elements if not i.startswith("\n")]
                for item in elements:
                    print(item)
                print(time)
                print("----------------------------")

    def read_editorials(self):
        if self.input_args in ["latest", "l"]:
            self.get_latest_editorial()
        if self.input_args in ["specific", "s"]:
            self.get_specific_editorial()


if __name__ == "__main__":
    urls = {"hindu": "http://www.thehindu.com/opinion/editorial/"}
    scraper = HinduScraper(urls)
    scraper.read_editorials()
