# program name  : Hindu Editorial scraper
# date          : Mon Jul 10 00:25:10 IST 2017

import re
import requests
from bs4 import BeautifulSoup
import urllib.request

# functions

def remove_tags(text):
    return tag_re.sub('', text)

###############

response = requests.get('http://www.thehindu.com/opinion/editorial/')
page1 = response.content
soup = BeautifulSoup(page1, "lxml")
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
    except:
        pass

# for link in editorial_links:
#     print(link)
# print(editorial_links)
tag_re = re.compile(r'<[^>]+>')

print("\n Welcome to Hindu Editorial scraper \n")
user_input = input("latest(l) | specific(s)\n:>")

if user_input == "latest" or user_input == "l":
    editorial_count = int(input("how many editorials you want to read\n:>"))
    print("---------------------------------------")
    i = 0
    while editorial_count > 0:
        response = requests.get(editorial_links[i])
        # print(editorial_links[i])
        page2 = response.content
        soup = BeautifulSoup(page2, "lxml")
        content = soup.findAll("p")
        # print(type(content[0]))
        print("Editorial " + str(i + 1) + "\n")
        print(remove_tags(str(content[0])))
        print("---------------------------------------")
        i += 1
        editorial_count -= 1

elif user_input == "specific" or user_input == "s":
    editorial_number = int(input("Which editorial do you want to read\n:>"))
    if editorial_number > 0:
        response = requests.get(editorial_links[editorial_number - 1])
        page2 = response.content
        soup = BeautifulSoup(page2, "lxml")
        content = soup.findAll("p")
        print("----------------------------")
        print(remove_tags(str(content[0])))
        print("----------------------------")

else:
    print("Invalid input")
