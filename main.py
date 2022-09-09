import flask

a = flask.__version__
print(a)
from flask import Flask
app = Flask(__name__) # Flask instance named app
