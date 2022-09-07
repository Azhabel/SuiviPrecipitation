import requests

from GPS import GPS


class Weather:

    def __init__(self, city_name):
        self.gps = GPS(city_name)


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
