# program name  : Hindu Editorial scraper
# date          : Mon Jul 10 00:25:10 IST 2017

import requests
from bs4 import BeautifulSoup
import urllib.request

response = requests.get('http://www.thehindu.com/opinion/editorial/')
page1 = response.content
soup = BeautifulSoup(page1, "lxml")
links = soup.findAll("a")

editorial_links = []
for link in links:
    try:
        if 'opinion/editorial' in link.get('href'):
            s = link.get('href')
            if s.endswith(".ece"):
                editorial_links.append(s)
    # print(type(link.get('href')))
    except:
        pass

# for link in editorial_links:
#     print(link)
# print(editorial_links)

editorial_count = int(input("how many editorials you want to read\n"))
i = 0
while editorial_count > 0:
    response = requests.get(editorial_links[i])
    # print(editorial_links[i])
    page2 = response.content
    soup = BeautifulSoup(page2, "lxml")
    content = soup.findAll("p")
    print(content[0])
    i += 1
    editorial_count -= 1
    print("---------------------------------------")
