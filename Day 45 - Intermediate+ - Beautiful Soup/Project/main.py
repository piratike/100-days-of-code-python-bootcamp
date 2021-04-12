# Code for Day 45 Project

import requests
from bs4 import BeautifulSoup

movies_webpage = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(movies_webpage.text, 'html.parser')
films = soup.find_all(name='div', class_='listicle-item')

titles = []

for film in films:

    titles.append(film.find(name='img').get('alt'))

titles.reverse()

with open('./Day 45 - Intermediate+ - Beautiful Soup/Project/movies.txt', 'w') as file:
    for movie in titles:
        file.write(f'{movie}\n')
