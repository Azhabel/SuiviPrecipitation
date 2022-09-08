import unittest
from datetime import date, timedelta

from Weather import Weather


class WeatherTest(unittest.TestCase):
    def test_precipitation_average(self):
        weather_forecast = Weather("Paris")
        today = date.fromisoformat("2022-09-07")
        next_week = today + timedelta(7)
        self.assertEqual(weather_forecast.precipitation_average(today, next_week), 2.8625)

    def test_current_weather(self):
        weather_forecast = Weather("Alès")
        current_weather = weather_forecast.current_weather()
        temperature = float(current_weather[0])
        weather_code = int(current_weather[1])
        self.assertTrue(len(current_weather), 2)
        self.assertGreater(temperature, -20.0)
        self.assertLess(temperature, 60.0)
        self.assertGreater(weather_code, -1)
        self.assertLess(weather_code, 100)
