from random import randint
import requests
from datetime import datetime

GENDER = "male"
AGE = randint(20, 30)
WEIGHT_KG = randint(50, 70)
HEIGHT_CM = randint(180, 200)

API_ID = "secret"
API_KEY = "secret"
TOKEN="secret"


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {"x-app-id": API_ID, "x-app-key": API_KEY}


nutritionix_params = {
    "query": input("What exercise did you do today?: "),
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}


nutritionix = requests.post(nutritionix_endpoint,json=nutritionix_params,headers=nutritionix_headers)
result=nutritionix.json()
print(result)

today=datetime.now().strftime('%d/%m/%Y')
now=datetime.now().strftime('%X')

sheety_endpoint="secret"
for exercise in result["exercises"]:
    sheety_params={
    "workout": {
        "date":today,
        "time":now,
        "exercise":exercise["name"].title(),
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"]
    }
    } 
bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}

sheet_response=requests.post(sheety_endpoint,json=sheety_params,headers=bearer_headers)
print(sheet_response.text)
