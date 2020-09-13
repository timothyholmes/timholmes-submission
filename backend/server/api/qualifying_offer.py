from resource.offers import get_qualifying, get_player_list


def get():
    players = get_player_list("https://questionnaire-148920.appspot.com/swe/data.html")
    offer = get_qualifying(players)

    return {
        "qualifying_offer": {"value": offer, "label": "${:,.2f}".format(offer)},
        "salaries": players.get_salaries(),
    }
