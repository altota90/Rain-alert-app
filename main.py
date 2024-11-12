import requests
from twilio.rest import Client

api_key = "9a6088cb2a4230ed4b9f96e67ac598df"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC0fc6c29a5d24bf888a18ab5ac61d51d8"
auth_token = "0beb0ae83ecd4b9678712a0c3da9b3b3"

weather_params = {
    "lat": 50.994892,
    "lon": -0.098077,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_='+447380328065',
        to='+447826698249'
    )
    print(message.status)








