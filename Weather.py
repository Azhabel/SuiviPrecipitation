import weakref
import requests

from GPS import GPS
from datetime import date, timedelta

city_name = "Paris"
today = date.today()
next_week = today + timedelta(7)
last_week = today - timedelta(7)


class Weather:

    def __init__(self, city_name, api_key):
        self.gps = GPS(city_name, api_key)

    def current_weather(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(self.gps.latitude()) + "&longitude=" \
              + str(self.gps.longitude()) + \
              "&current_weather=true"
        request = requests.get(url)
        current_weather_data = request.json()["current_weather"]
        return current_weather_data

    def current_weather_degree(self):
        return self.current_weather()["temperature"]

    def current_weather_cloud(self):
        return self.current_weather()["weathercode"]

    def precipitation_average(self, first_day, last_day):
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(self.gps.latitude()) + "&longitude=" \
              + str(self.gps.longitude()) + \
              "&daily=precipitation_sum&timezone=Europe%2FBerlin&start_date=" + \
              str(first_day) + "&end_date=" + str(last_day)
        request = requests.get(url)
        json = request.json()
        precipitations = json["daily"]["precipitation_sum"]
        avg = 0
        number_of_values = 0
        for value in precipitations:
            if value is not None:
                avg += value
            number_of_values += 1

        avg = avg / number_of_values
        return avg
    
    def last_week_precipitation(self):
        return self.precipitation_average(last_week, today)
    
    def next_week_precipitation(self):
        return self.precipitation_average(today, next_week)