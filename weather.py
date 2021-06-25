# import requests
# from datetime import datetime
#
# api_key ="5246ca420132b2527b4127214cfb2d2d"
# location = input("Enter your city name:  ")
#
# api_link = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
# api_link = requests.get(api_link)
# api_data = api_link.json()
#
# temp_city = ((api_data['main']['temp']) - 273.15)
# weather_description = api_data['Weather'][0]['Description']
# humidity = api_data['main']['Humidity']
# wind_speed = api_data['wind']['speed']
# date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
#
# print("Weather states for - {} || {}".format(location.upper(),date_time))
#
# print("Current temperature is :{:.2f} deg C".format(temp_city))
# print("Current weather description is :", weather_description)
# print("Current humidity is :" ,humidity,'%')
# print("Current wind speed is :", wind_speed,'kmph')
#
import requests
#import os
from datetime import datetime

api_key = '5246ca420132b2527b4127214cfb2d2d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')