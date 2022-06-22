from xo import *
from flask import Flask

app = Flask(__name__)

@app.route('/<text>')
def my_view_func(text):
    return "!!!"+text+"!!!"
  
@app.route('/')
def hello():
    return 'Hello, World!'
