# Code for Day 46 Project

import requests, datetime, spotipy, pprint
from bs4 import BeautifulSoup

DATE_OK = False
SPOTIFY_CLIENT_ID = '2dd6a9e37c004989ae66a36134b229da'
SPOTIFY_CLIENT_SECRET = 'c37b54725c594146b5deee78db8fa347'

spotify_access = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = spotify_access.current_user()["id"]

while not DATE_OK:

    date = input('Wich date do you want to travel to? (Type the date in YYYY-MM-DD format): ')
    required_format = '%Y-%m-%d'

    try:

        datetime.datetime.strptime(date, required_format)
        DATE_OK = True

    except ValueError:

        print('Incorrect date format!')
        DATE_OK = False

billboard_webpage = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
billboard_soup = BeautifulSoup(billboard_webpage.text, 'html.parser')

songs = [song.getText() for song in billboard_soup.find_all(name='span', class_='chart-element__information__song')]
song_uris = []
year = date.split('-')[0]

for song in songs:

    song_finded = spotify_access.search(q=f'track:{song} year: {year}', type='track')

    try:

        uri = song_finded['tracks']['items'][0]['uri']
        song_uris.append(uri)

    except IndexError:

        pass

spotify_playlist = spotify_access.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
spotify_access.playlist_add_items(playlist_id=spotify_playlist['id'], items=song_uris)
