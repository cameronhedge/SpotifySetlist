import requests

URL = "https://deezerdevs-deezer.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": "cd79e655b9msh46f8c56d1921c9ep1bc6f1jsnbf77ea1ba296",
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}


def get_deezer_id(song, artist):
    url = f'{URL}/search'
    q = {'q': f'artist:"Judas Priest\""living after midnight"'}

    response = requests.get(url, headers=HEADERS, params=q)

    if len(response.json()['data']) < 1:
        print(f"NO RESULTS FOR {song}")
        return

    return response.json()['data'][0]['id']



def get_isrc(deezer_id):
    url = f'{URL}/track/{deezer_id}'
    response = requests.get(url, headers=HEADERS)

    return response.json()['isrc']
