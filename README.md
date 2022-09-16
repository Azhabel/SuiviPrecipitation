<h1>Precipitation / weather monitoring</h1>

<h3>Description</h3>

This app allows you to check the weather in any town or city.

<h3>Features</h3>

You can enter a city name in the search bar, and press enter to display information about the weather:
 - The current weather, with an icon that represents it,
 - The average amount of last week's precipitation (in mm),
 - The average amount of next week's precipitation (in mm).

<h3>How to run locally</h3>
Install flask:
``
pip install flask
``

Set the FLASK_APP and FLASK_ENV environment variables:

````
export FLASK_APP=main
export FLASK_ENV=development
````

Run the app:
``flask run``

You can access the app in your browser on the 5000 port.