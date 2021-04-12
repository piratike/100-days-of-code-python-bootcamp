# Code for Day 45 Practice

from os import name
from bs4 import BeautifulSoup

# Scraping File -----------------------------------------------------------------------------------

# with open('./Day 45 - Intermediate+ - Beautiful Soup/Practice/website.html', encoding='utf-8') as file:

#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# print(soup)
# print(soup.title.name)
# print(soup.title.string)

# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag.get('href'))

# class_is_heading = soup.find_all(class_='heading')
# print(class_is_heading)

# h3_heading = soup.find_all('h3', class_='heading')
# print(h3_heading)

# name = soup.select_one('#name')
# print(name)

# headings = soup.select('.heading')
# print(headings)

# Scraping Live Website ---------------------------------------------------------------------------

import requests

yc_webpage = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(yc_webpage.text, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')

article_texts = []
article_links = []

for article_tag in articles:

    article_texts.append(article_tag.string)
    article_links.append(article_tag.get('href'))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
largest_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_index], article_links[largest_index])
