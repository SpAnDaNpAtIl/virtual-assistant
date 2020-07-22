import requests
import json
import re
from bs4 import BeautifulSoup as bsoup

url_for_ip_location = 'http://ipinfo.io/json'
response = requests.get(url_for_ip_location)
data = response.json()

IP_address=data['ip']

API_key = '562bcf71194e47949d2140655202207'
weather_url = 'http://api.weatherapi.com/v1/current.json'
data_weather = {'key':API_key, 'q':IP_address}

weather_data = requests.post(weather_url, data=data_weather)
kp_weather = weather_data.json()

def current_temp():
    return kp_weather.get('current').get('temp_c')


def status_of_weather():
    return kp_weather.get('current').get('condition').get('text')


def wind_speed():
    return kp_weather.get('current').get('wind_kph')


def humidity():
    return kp_weather.get('current').get('humidity')

