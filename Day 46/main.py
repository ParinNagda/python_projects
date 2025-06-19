from os import environ

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=environ.get("CLIENT_ID"),
        client_secret=environ.get("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
print(url)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="lrv-u-font-size-16")

song_uris = []
year = date.split("-")[0]
for song in song_names:
    song = song.getText().strip()
    print(song)
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
