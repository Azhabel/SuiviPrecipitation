from datetime import date, timedelta

from Weather import Weather

forecast = Weather("Paris")
today = date.today()
next_week = today + timedelta(7)
print(forecast.precipitation_average(today, next_week))