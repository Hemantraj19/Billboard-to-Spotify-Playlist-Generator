from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_input = input("Which year do yo want to travel to? Type the date in this format YYYY-MM-DD: ")

# ----------------------------- Scrape the website ------------------------------------
url_endpoint = f"https://www.billboard.com/charts/hot-100/{date_input}/"

response = requests.get(url=url_endpoint)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, 'lxml')

top_100_song_h3 = soup.select(selector="li ul li h3")

top_100_song_title = []
for title in top_100_song_h3:
    top_100_song_title.append(str(title.getText()).strip())

print(len(top_100_song_title))
# ---------------------------------------------------------------------------------

# ========================== Authenticate Spotify =================================
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id="",
        client_secret="",
        redirect_uri="https://www.example.com",
        show_dialog=True,
        cache_path="token.txt",
        username=""))

user_id = sp.current_user()["id"]
# ==================================================================================

# ----------------------------- Make songs URI -------------------------------------
song_uris = []
year = date_input.split("-")[0]
for song in top_100_song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# ----------------------------------------------------------------------------------

# =========================== Create And Add Playlist ==============================
playlist = sp.user_playlist_create(user_id, f"{date_input} Billboard 100", public=False)
sp.playlist_add_items(playlist['id'], song_uris)
print("Songs Added Successfully. Enjoy!")
