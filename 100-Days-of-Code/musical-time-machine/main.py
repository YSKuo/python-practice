import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = "http://example.com"
scope = "playlist-modify-private"

time = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")

url = "https://www.billboard.com/charts/hot-100"

response = requests.get(url=f"{url}/{time}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")

song_tags = soup.select(".chart-element__information__song")

song_titles = [tag.getText() for tag in song_tags]

# print(song_titles)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    show_dialog=True,
))

user_id = sp.current_user()["id"]

YYYY = time[0:4]
song_uris = []

for song in song_titles:
    query = f"track: {song} year: 2000"
    result = sp.search(query, type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)


playlist_name = f"{time} Billboard 100"
playlist = sp.user_playlist_create(
    user=user_id, name=playlist_name, public=False)


result = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

pprint(result)
