KEY = "key_here"
CITY = "Portsmouth"
CALL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},uk&appid={KEY}"

import requests

REQUEST = requests.get(CALL)
WEATHER = REQUEST.json()

#print(WEATHER)

for index in WEATHER:
  SPACES = " " * (10-len(index))
  print(f"{index} {SPACES}: {WEATHER[index]}")
