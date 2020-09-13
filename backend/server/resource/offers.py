import requests
from statistics import mean
from bs4 import BeautifulSoup
from models.player import Player
from models.player_list import PlayerList

# https://realpython.com/beautiful-soup-web-scraper-python/
def get_player_list(url):
    try:
        page = requests.get(url)
    except:
        print('Error! Could not get file at url:', url)
        return PlayerList([])

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(id="salaries-table")
    rows = table.find_all("tr")

    player_list = []

    for row in rows:
        cells = row.find_all("td")
        player_info = {}

        for cell in cells:
            player_info[cell.attrs["class"][0]] = cell.text

        player_list.append(
            Player(
                name=player_info["player-name"],
                salary=player_info["player-salary"],
                year=player_info["player-year"],
                level=player_info["player-level"],
            )
        )

    return PlayerList(player_list)


# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
# https://stackoverflow.com/questions/538551/handling-very-large-numbers-in-python
def get_qualifying(players):
    salaries = players.get_salaries()

    if len(salaries)  > 0:
        return mean(salaries[:123])

    return 0