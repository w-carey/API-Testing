KEY = "KEY_HERE"
CITY = "Portsmouth"
CALL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},uk&appid={KEY}"

import requests

REQUEST = requests.get(CALL)
WEATHER = REQUEST.json()

#print(WEATHER)

for index in WEATHER:
  print(index, ":", WEATHER[index])
