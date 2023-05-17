from os import environ as env
import requests
from datetime import date, datetime

EXERCISE_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_URL = 'https://api.sheety.co/ebc0ce7d259ee43171eee36272ae4259/myWorkouts/workouts'
APP_ID = env['NUTRITIONIX_APPID']
API_KEY = env['NUTRITIONIX_APIKEY']
MY_EMAIL = env['MY_EMAIL']
SHEETY_AUTHTOKEN = env['SHEETY_AUTHTOKEN']
time = datetime.now().strftime('%H:%M:%S')
date = date.today().strftime('%d/%m/%Y')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '1'
}

parameters = {
    'query': input("What exercise did you do?\n")
}

exercise_request = requests.post(url=EXERCISE_URL, json=parameters, headers=headers)
exercise_request.raise_for_status()
exercise_data = exercise_request.json()['exercises'][0]
exercise = exercise_data['user_input']
duration = exercise_data['duration_min']
calories = exercise_data['nf_calories']
headers = {
    'Authorization': f'Bearer {SHEETY_AUTHTOKEN}'
}

data = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

request = requests.post(url=SHEETY_URL, json=data, headers=headers)
request.raise_for_status()


