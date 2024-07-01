import requests

RANDOM_WORD_API_URL = "https://www.wordgamedb.com/api/v1/words/"


def get_word_list():
    data = requests.get(RANDOM_WORD_API_URL, ).json()
    return [{"word": word["word"], "hint": word["hint"]} for word in data]
