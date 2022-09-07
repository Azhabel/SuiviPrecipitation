import unittest
from datetime import date, timedelta

from Weather import Weather


class WeatherTest(unittest.TestCase):
    def test_precipitation_average(self):
        forecast = Weather("Paris")
        today = date.fromisoformat("2022-09-07")
        next_week = today + timedelta(7)
        self.assertEqual(forecast.precipitation_average(today, next_week), 2.8625)