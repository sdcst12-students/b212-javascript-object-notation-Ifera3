#!Python 3

#site https://open-meteo.com/en/docs

import json, requests

"""
info from: https://api.open-meteo.com/v1/forecast?latitude=48.4359&longitude=-123.3516&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum&timezone=America%2FLos_Angeles

reciving for Victora BC weather:
max day temp (C)
min day temp (C)
amount of parcipitation (mm)
UV index
sunrise
sunset
"""


def main():
    req = requests.get('https://api.open-meteo.com/v1/forecast?latitude=48.4359&longitude=-123.3516&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum&timezone=America%2FLos_Angeles')
    theData = req.text
    #print(theData)
    weatherinfo = json.loads(theData)
    print("┌────────────────────────────────────────────────────────────────────────────┐")
    print("│                Weather in Victory for the next seven days                  │")
    print("│────────────┬──────────┬──────────┬───────────┬──────────┬─────────┬────────┤")
    print("│    Date    │ Temp Max │ Temp Min │ Rain Fall │ UV index │ Sunrise │ Sunset │")
    for i in range(len(weatherinfo['daily']['time'])):
        print("│────────────┼──────────┼──────────┼───────────┼──────────┼─────────┼────────┤")
        print(f"│ {weatherinfo['daily']['time'][i]} │  {f'{weatherinfo['daily']['temperature_2m_max'][i]} C':<6}  │  {f'{weatherinfo['daily']['temperature_2m_min'][i]} C':<6}  │  {f"{weatherinfo['daily']['precipitation_sum'][i]} mm":<7}  │   {weatherinfo['daily']['uv_index_max'][i]:<5}  │  {weatherinfo['daily']['sunrise'][i].replace(f'{weatherinfo['daily']['time'][i]}T','')}  │ {weatherinfo['daily']['sunset'][i].replace(f'{weatherinfo['daily']['time'][i]}T','')}  │")
    print("│────────────┼──────────┼──────────┼───────────┼──────────┼─────────┼────────┤")


if __name__ == '__main__':
    main()