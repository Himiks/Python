import requests
from datetime import datetime
APP_ID ="yours"
API_KEY = "yours"
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 149
AGE = 27


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did:")

header = {
	"x-app-id": APP_ID,
	"x-app-key": API_KEY
}

parametrs = {
	"query": exercise_text,
	"gender": GENDER,
	"weight_kg": WEIGHT_KG,
	"height_cm": HEIGHT_CM,
	"age": AGE
}

response = requests.post(exercise_endpoint, json=parametrs, headers=header)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
	sheet_inputs = {
	"workout":{
		"date": today_date,
		"time": now_time,
		"exercise": exercise["name"].title(),
		"duration": exercise["duration_min"],
		"calories": exercise["nf_calories"]

	}
	}
	sheet_endpoint=""
	sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)