import weakref
import requests

from GPS import GPS
from datetime import date, timedelta

today = date.today()
next_week = today + timedelta(7)
last_week = today - timedelta(7)


class Weather:

    def __init__(self, city_name, api_key):
        print("City: ", city_name)
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
        wcode = self.current_weather()["weathercode"]
        wlogo = ""
        if wcode == 0:
            wlogo = "sun"
        elif wcode >= 1 and wcode <= 44:
            wlogo = "sunny_cloud"
        elif wcode >= 45 and wcode <= 50:
            wlogo = "cloud"
        elif wcode >= 51 and wcode <= 70:
            wlogo = "rainy_cloud"
        elif wcode >= 71 and wcode <= 79:
            wlogo = "snowy_cloud"
        elif wcode >= 80 and wcode <= 84:
            wlogo = "rainy_cloud"
        elif wcode >= 85 and wcode <= 94:
            wlogo = "snowy_cloud"
        elif wcode >= 95 and wcode <= 100:
            wlogo = "rainy_cloud"
        else:
            wlogo = "waiting_weather"
        return wlogo

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
        print("avg last: ", self.precipitation_average(last_week, today))
        return self.precipitation_average(last_week, today)
    
    def next_week_precipitation(self):
        print("avg next: ", self.precipitation_average(today, next_week))
        return self.precipitation_average(today, next_week)
