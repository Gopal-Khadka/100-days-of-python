import requests

input = {
    "amount": 5,
    "type": "boolean",
    "category": 18,
}


data = requests.get(url="https://opentdb.com/api.php", params=input)
data.raise_for_status()
question_data = data.json()["results"]

if __name__ == "__main__":
    print(question_data)
