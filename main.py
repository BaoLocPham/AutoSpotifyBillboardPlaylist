import os
from Utils import *

# dunno man, there's a library for spotify :))
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from termcolor import colored


def create_list_song_uri(song_names_list, artist_names_list):

    song_uri_list = []
    for song_name, artist_name in zip(song_names_list, artist_names_list):
        results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track")
        try:
            song_uri = results['tracks']['items'][0]['uri']
            print(colored(f"Found uri for song {song_name}", 'green'))
            song_uri_list.append(song_uri)
        except IndexError:
            print(colored(f"Not found uri for song {song_name} => skip this song.", 'red'))
    return song_uri_list


if __name__ == '__main__':
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']

    # if you want your playlist to public -> change it to public
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri="http://example.com",
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    date = get_date()
    song_names, artist_names = create_list_song(date)
    song_uris = create_list_song_uri(song_names, artist_names)

    user_id = sp.current_user()["id"]
    print(user_id)
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboad {date}", public=False, description='No description')
    print(playlist)

    playlist_id = playlist['id']

    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

