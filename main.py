from email.errors import CloseBoundaryNotFoundDefect
from flask import Flask, render_template, request, make_response, redirect, url_for
from Weather import Weather

api_key = "d62c1a3f25d595fdad7c00363298ba2f"


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/index')
@app.route('/') 
def homepage():
    return render_template("index.html")

@app.route('/search', methods =['GET', 'POST'])
def searchCity():
    city_input = ""
    if request.method == "POST":
       city_input = request.form.get('city_searched')
       print("city_input: ", city_input)
    weather = Weather(str(city_input), api_key)
    return render_template('search.html', 
        city = city_input,
        last_week_previs = weather.last_week_precipitation(),
        today_previs_degree = weather.current_weather_degree(),
        next_week_previs = weather.next_week_precipitation(),
        weather_logo = weather.current_weather_cloud()
    )

@app.errorhandler(404)
def handle_bad_request(e):
    return redirect(url_for('index'))


@app.errorhandler(405)
def handle_methodnotallowed_request(e):
    return redirect(url_for('index'))
