import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

SPOTIPY_CLIENT_ID = '89af0212dca14682871775077117dfe9'
SPOTIPY_CLIENT_SECRET = '074545463400498388abfbfba76d97be'
SPOTIPY_REDIRECT_URI = 'http://example.com'

scope = 'playlist-modify-private, playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope = scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))

