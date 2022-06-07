import requests
from pprint import pprint

h = {'accept' : 'application/json'}

def getMbid(artist):
    params = {'query': str(artist)}
    response = requests.get(url='https://musicbrainz.org/ws/2/artist', params=params, headers=h)
    result = response.json()
    artists = []
    for artist in result['artists'][:5]:
        artists.append({
            'name' : artist['name'],
            'id' : artist['id']
        })
    return artists