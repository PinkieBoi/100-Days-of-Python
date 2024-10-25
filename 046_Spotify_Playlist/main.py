import os
import pprint
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from nested_lookup import nested_lookup
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

period = input("Enter a memorable date to create the playlist (YYYY-MM-DD): ")
billboard_url = "https://www.billboard.com/charts/hot-100/" + period
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

res = requests.get(url=billboard_url, headers=header).text
soup = BeautifulSoup(res, "html.parser")
hits = soup.select("li ul li h3")
song_titles = [hit.getText().strip() for hit in hits]

# Spotify Auth
REDIRECT_URI = "http://localhost:3000/callback"
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ['SPOTIFY_CLIENT_ID'],
        client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
        redirect_uri="http://example.com",
        scope=scope,
        show_dialog=True,
        cache_path="./token.txt"
        # username=os.environ['SPOTIFY_USERNAME'],
    )
)
user_id = sp.current_user()["id"]

pp = pprint.PrettyPrinter(indent=4)
uri_values = []
for song in song_titles:
    data = sp.search(q=f"track:{song} year:{period.split("-")[0]}",
                     type="track")
    for uri in nested_lookup('uri', data):
        if uri.split(":")[1] != "track":
            continue
        if uri not in uri_values:
            uri_values.append(uri)

print(uri_values)
print(len(uri_values))

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{period} Billboard 100",
    public=False,
    collaborative=False,
    description="Playlist created using the top 100 songs during major life events"
                " or whatever date you pulled out of your rear :p"
)

populate_list = sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=uri_values
)
