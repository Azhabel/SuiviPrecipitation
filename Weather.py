from datetime import date, timedelta

import requests

from GPS import GPS

today = date.today()
next_week = today + timedelta(7)
last_week = today - timedelta(7)


class Weather:

    def __init__(self, city_name, api_key):
        print("City: ", city_name)
        self.gps = GPS(city_name, api_key)

    def current_weather(self):
        try:
            url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(self.gps.latitude()) + "&longitude=" \
              + str(self.gps.longitude()) + \
              "&current_weather=true"
            request = requests.get(url)
            request.raise_for_status()
            current_weather_data = request.json()["current_weather"]
            return current_weather_data
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def current_weather_degree(self):
        return self.current_weather()["temperature"]

    def current_weather_cloud(self):
        wcode = self.current_weather()["weathercode"]
        wlogo = ""
        if wcode == 0:
            wlogo = "sun"
        elif 1 <= wcode <= 44:
            wlogo = "sunny_cloud"
        elif 45 <= wcode <= 50:
            wlogo = "cloud"
        elif 51 <= wcode <= 70:
            wlogo = "rainy_cloud"
        elif 71 <= wcode <= 79:
            wlogo = "snowy_cloud"
        elif 80 <= wcode <= 84:
            wlogo = "rainy_cloud"
        elif 85 <= wcode <= 94:
            wlogo = "snowy_cloud"
        elif 95 <= wcode <= 100:
            wlogo = "rainy_cloud"
        else:
            wlogo = "waiting_weather"
        return wlogo

    def precipitation_average(self, first_day, last_day):
        try:
            url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(self.gps.latitude()) + "&longitude=" \
            + str(self.gps.longitude()) + \
            "&daily=precipitation_sum&timezone=Europe%2FBerlin&start_date=" + \
            str(first_day) + "&end_date=" + str(last_day)
            request = requests.get(url)
            request.raise_for_status()
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
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
    
    def last_week_precipitation(self):
        print("avg last: ", self.precipitation_average(last_week, today))
        return self.precipitation_average(last_week, today)
    
    def next_week_precipitation(self):
        print("avg next: ", self.precipitation_average(today, next_week))
        return self.precipitation_average(today, next_week)
