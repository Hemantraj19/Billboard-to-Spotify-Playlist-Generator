# Billboard to Spotify Playlist Generator

This Python script allows you to create a Spotify playlist based on the Billboard Hot 100 songs from a specific date.

## Prerequisites

1. Python installed on your machine.
2. Required Python packages installed:
   - BeautifulSoup (`pip install beautifulsoup4`)
   - Requests (`pip install requests`)
   - Spotipy (`pip install spotipy`)

## Usage

1. Run the script by executing the Python file.
2. Enter the desired date in the format `YYYY-MM-DD` when prompted.
3. The script will scrape the Billboard Hot 100 songs from the specified date.
4. You will be prompted to authenticate the script with your Spotify account.
5. The script will then search for each song on Spotify and create a private playlist for that date.
6. The songs will be added to the playlist on your Spotify account.

## Important Note

Make sure to replace the empty strings (`""`) in the script with your actual Spotify API credentials:

```python
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "your_redirect_uri"
username = "your_spotify_username"
```
The script attempts to find each song on Spotify based on its title and release year. Some songs may not be available on Spotify or may have different titles, causing them to be skipped.

The generated playlist is set to private by default. You can change this in the script by modifying the public parameter when creating the playlist.
