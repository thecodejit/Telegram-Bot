import requests

result = requests.get("https://api.covid19india.org/data.json")
src = result.json()

world = requests.get("https://api.covid19api.com/summary")
src2 = world.json()


def covid_india_data():
    """parsing the api an sending the result to bot.py"""
    for data in src['statewise']:
        # checking date and time with the API
        if (data['statecode']) == 'TT':
            daily_infected = data['deltaconfirmed']
            daily_cured = data['deltarecovered']
            daily_death = data['deltadeaths']

            total_infected = data['confirmed']
            total_active = data['active']
            total_cured = data['recovered']
            total_death = data['deaths']

            last_update = data['lastupdatedtime']

    return "Here Is The Recent Update", "\nAs of ", last_update, "\n\n\b\b", "     New Cases Today\n", "  Infected -", \
           daily_infected, "\n", "  Cured    -", daily_cured, "\n", "  Dead     -", \
           daily_death, "\n", "      All Total (Recurring)", "\n", "  Confirmed -", total_infected, "\n", \
           "  Active         -", total_active, "\n", "  Cured         -", total_cured, "\n", "  Dead          -", \
           total_death, "\n\n"


def split(word):
    return [char for char in word]


def covid_world_data():
    charc = ['T', 'Z']
    total_confirmed = src2['Global']['TotalConfirmed']
    total_active = src2['Global']['TotalRecovered']
    total_dead = src2['Global']['TotalDeaths']
    last_update = src2['Date']
    for i in charc:
        last_update = last_update.replace(i, ' ')
    return "Here Is The Recent Update", "\nAs of " + str(
        last_update) + "\n\n\b\b", "     Total Cases \n", "  Confirmed -" \
           + str(total_confirmed) + "\n", "  Recovered -" + str(total_active) + "\n", "  Dead          -" \
           + str(total_dead)
