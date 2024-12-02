#!Python 3

#site https://open-meteo.com/en/docs

import json, requests

"""
info from: https://api.open-meteo.com/v1/forecast?latitude=48.4359&longitude=-123.3516&hourly=temperature_2m,apparent_temperature,precipitation_probability,precipitation&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset

reciving:
temp (C)
fells like (C)
chance of parcipitation (%)
amount of parcipitation (mm)
max day temp (C)
min day temp (C)
sunrise
sunset
"""

req = requests.get('https://api.open-meteo.com/v1/forecast?latitude=48.4359&longitude=-123.3516&hourly=temperature_2m,apparent_temperature,precipitation_probability,precipitation&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset')
theData = req.text
print(theData)
weatherinfo = json.loads(theData)
print(f"┌────────────┬─────┐")
for i in weatherinfo['daily']['time']:
    print(f"│ {i} │ day │")