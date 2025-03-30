import requests
import json
from dateutil import tz
from datetime import datetime
from twilio.rest import Client
#---------------------------Constants----------------------------------------------#
account_sid = '******************************'
auth_token = '*******************************'
def rain_check(data):
    global account_sid
    global auth_token
    for (key,value) in data.items():
        if value<600:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
  												from_='+14707983677',
  												to='*************',
  												body=f"Carry an umbrella cuz its gonna rain. at {key}:00 hours today")
				
def time_coverter(data):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    real_time=[]
    for key in data:
        utc = datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        real_time.append(central.hour)
    return real_time
   

#Etobicoke,ON,Can
place="Etobicoke,ON,Can"
appkey='740d996b5cd91a6ecc830fddaa3d45db'
geocode_params={'q':place,
                'appid':appkey}
geocode_api=requests.get(url='http://api.openweathermap.org/geo/1.0/direct',params=geocode_params)
geocode=geocode_api.json()
with open("geocode.json",mode='w') as file:
    json.dump(geocode,file,indent=4)

dicto={'lat':geocode[0]['lat'],
'lon':geocode[0]['lon'],
'cnt':3,
'units':'metric',
'appid':appkey}
data=requests.get('https://api.openweathermap.org/data/2.5/forecast',params=dicto)
weather=data.json()
rain_data=[weather['list'][n]["dt_txt"] for n in range(0,3)]
print(weather)
hour_data=time_coverter(rain_data)
#:weather['list'][n]['weather'][0]['id']
#hourly_weather={hour_data[n]:weather['list'][n]['weather'][0]['id'] for n in range(0,3)}
#rain_check(hourly_weather)

with open("data.json",mode='w') as file:
    json.dump(weather,file,indent=4)
