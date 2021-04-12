# Code for Day 45 Practice

from bs4 import BeautifulSoup

with open('./Day 45 - Intermediate+ - Beautiful Soup/Practice/website.html', encoding='utf-8') as file:

    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup)
print(soup.title.name)
print(soup.title.string)

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.get('href'))

class_is_heading = soup.find_all(class_='heading')
print(class_is_heading)

h3_heading = soup.find_all('h3', class_='heading')
print(h3_heading)

name = soup.select_one('#name')
print(name)

headings = soup.select('.heading')
print(headings)
