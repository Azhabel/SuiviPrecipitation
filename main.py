from flask import Flask, render_template
from Weather import Weather

api_key = "d62c1a3f25d595fdad7c00363298ba2f"

app = Flask(__name__)
weather = Weather("Paris", api_key)


@app.route('/')
def index():
    return render_template('index.html', 
        city = "Paris",              
        last_week_previs = weather.last_week_precipitation(),
        today_previs_degree = weather.current_weather_degree(),
        next_week_previs = weather.next_week_precipitation()
        )