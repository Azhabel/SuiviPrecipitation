import unittest
from datetime import date, timedelta

from Weather import Weather


class WeatherTest(unittest.TestCase):
    api_key = "d62c1a3f25d595fdad7c00363298ba2f"

    def test_precipitation_average(self):
        weather_forecast = Weather("Paris", self.api_key)
        today = date.fromisoformat("2022-09-01")
        next_week = today + timedelta(7)
        self.assertGreaterEqual(weather_forecast.precipitation_average(today, next_week), 1.4)

    def test_current_weather(self):
        weather_forecast = Weather("Alès", self.api_key)
        current_weather = weather_forecast.current_weather()
        temperature = float(current_weather["weathercode"])
        weather_code = int(current_weather["temperature"])
        self.assertTrue(len(current_weather), 2)
        self.assertGreater(temperature, -20.0)
        self.assertLess(temperature, 60.0)
        self.assertGreater(weather_code, -1)
        self.assertLess(weather_code, 100)
