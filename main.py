from email.errors import CloseBoundaryNotFoundDefect
import sunau
from flask import Flask, render_template, request
from Weather import Weather

api_key = "d62c1a3f25d595fdad7c00363298ba2f"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods =['GET', "POST"])
def searchCity():
    city_input = ""
    if request.method == "POST":
       city_input = request.form.get("city_searched")
       print("city_input: ", city_input)
    weather = Weather(str(city_input), api_key)
    return render_template("index.html", 
        city = city_input,
        last_week_previs = weather.last_week_precipitation(),
        today_previs_degree = weather.current_weather_degree(),
        next_week_previs = weather.next_week_precipitation(),
        weather_logo = weather.current_weather_cloud()
    )