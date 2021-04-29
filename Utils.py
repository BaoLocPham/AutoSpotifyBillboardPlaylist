from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup


def get_date():
    today_ = dt.today()
    today = today_.date()
    input_date = input("Which year you want to travel? Type the date in this format YYYY-MM-DD: (default is today)")
    try:
        date = dt.strptime(input_date, "%Y-%m-%d")
        if date > today:
            input_date = today
    except ValueError:
        input_date = today
    return str(input_date)


def create_list_song(input_date:str):

    href = "https://www.billboard.com/charts/hot-100/"

    response = requests.get(href+input_date)

    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    songs_ = soup.find_all("span", {"class": "chart-element__information__song text--truncate color--primary"})
    song_names_list = [song.getText() for song in songs_]
    artists_ = soup.find_all("span", {"class": "chart-element__information__artist text--truncate color--secondary"})
    artist_names_list = [artist.getText() for artist in artists_]

    return song_names_list, artist_names_list