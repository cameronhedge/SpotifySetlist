from repertorio import Repertorio
from pprint import pprint
from mbid import getMbid

API_KEY = 'iak-1wyfR1g9DBHGP-sMTEygP5bgCK3AHgzY'

api = Repertorio(API_KEY)

test = api.artist_setlists(getMbid('Guns n Roses'))

pprint(test['setlist'])