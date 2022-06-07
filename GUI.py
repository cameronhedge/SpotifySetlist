from tkinter import *
from tkinter import ttk
from mbid import getMbid
from main import makePlaylist

global LISTED_ARTISTS
global SELECTED_ARTIST

def searchArtist():
    global LISTED_ARTISTS
    LISTED_ARTISTS = getMbid(search.get())
    values = tuple(artist['name'] for artist in LISTED_ARTISTS)
    artist_select['values'] = values

def confirmArtist():
    global SELECTED_ARTIST
    SELECTED_ARTIST = LISTED_ARTISTS[artist_select.current()]


root = Tk()
root.title("Spotify - Live Playlist Creator")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

artist = ttk.Label(mainframe, text = "Artist", padding = 5).grid(column = 0, row = 0, rowspan = 2, sticky = (N, E, S, W))

search = StringVar()
search_entry = ttk.Entry(mainframe, textvariable = search).grid(column = 1, row = 0, sticky = (N, E, S, W))

artist_select = ttk.Combobox(mainframe, state = 'readonly')
artist_select.grid(column = 1, row = 1, sticky = (N, E, S, W))

search_button = ttk.Button(mainframe, text = "SEARCH", command = searchArtist).grid(column = 2, row = 0)
confirm_button = ttk.Button(mainframe, text = "CONFIRM", command = confirmArtist).grid(column = 2, row = 1)
confirm_button = ttk.Button(mainframe, text = "PLAYLIST", command = lambda: makePlaylist(SELECTED_ARTIST['name'], int(number_spin.get()),SELECTED_ARTIST['id'])).grid(column = 2, row = 2)

number_label = ttk.Label(mainframe, text = "No of Setlists").grid(row = 2, column = 0)
number = IntVar()
number_spin = ttk.Spinbox(mainframe, from_ = 1, to = 20, textvariable = number, width = 5)
number_spin.grid(row = 2, column = 1, sticky = (E))


root.mainloop()