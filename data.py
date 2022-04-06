import requests


parameters = {
    "amount": 10,
    "type": "boolean"
}
question_data = []
data = requests.get(url="https://opentdb.com/api.php", params=parameters)
data.raise_for_status()
print(data.json()["results"])
for item in data.json()["results"]:
    item["question"] = item["question"].replace('&quot;', '"')
    item["question"] = item["question"].replace('&#039;', "'")
    question_data.append(item)

