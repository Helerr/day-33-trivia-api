import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(url="https://opentdb.com/api.php", params=parameters)
data.raise_for_status()

question_data = html.unescape(data.json()["results"])
