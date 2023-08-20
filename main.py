import requests
import json
from mbid import getMbid
from pprint import pprint
from spotify_auth import sp
from spotipy import SpotifyException
import urllib

SPOTIFY_USER_ID = sp.me()['id']

h = {'x-api-key': 'iak-1wyfR1g9DBHGP-sMTEygP5bgCK3AHgzY', 'accept' : 'application/json'}

def getSetlists(artist_id, number):
    response = requests.get(url='https://api.setlist.fm/rest/1.0/artist/{}/setlists'.format(artist_id), headers=h)
    response.raise_for_status()
    setlist = response.json()['setlist'][:number]
    return sortSetlists(setlist)

def sortSetlists(setlist):
    all_setlists = []
    for set in setlist:
        full_setlist = set['sets']['set']
        all_songs = []
        for small_set in full_setlist:
            for song in small_set['song']:
                all_songs.append(song['name'])
        all_setlists.append(all_songs)
    # Returns a list for each gathered setlist
    return all_setlists

def compileSongs(setlists, artist_name):
    # All songs compiled
    all_songs = []

    for song_set in setlists:
        for song in song_set:
            all_songs.append(song)

    # All songs no duplicates
    no_duplicates = list(set(all_songs))
    setlist_data = []

    for song in no_duplicates:
        setlist_data.append({
            'song-name' : song,
            'occurences' : all_songs.count(song),
            'spotify-id' : getTrackSpotifyId(song, artist_name)
        })

    sortedData = sorted(setlist_data, key=lambda d: d['occurences'], reverse = True)

    return sortedData

def getTrackSpotifyId(name, artist):
    if name == None or name == '':
        return
    name = urllib.parse.quote_plus(name)
    artist = urllib.parse.quote_plus(artist)
    query_string = f'{name}%20artist:{artist}'

    track = sp.search(q = query_string, type = 'track', limit = 1)

    try:
        track_id = track['tracks']['items'][0]['id']
    except IndexError:
        track_id = None

    return track_id

def makePlaylist(artist_name, number, artist_id):
    playlist_name = (artist_name + " Live")
    setlists = getSetlists(artist_id, number)
    songs = compileSongs(setlists, artist_name)
    pprint(songs)
    #playlist_id = sp.user_playlist_create(user = SPOTIFY_USER_ID, name = playlist_name, public = False)['id']

    for song in songs:
        track = [song['spotify-id']]
        if track[0] == None:
            continue
        # sp.playlist_add_items(playlist_id, track)
    print("PLAYLIST CREATED")



