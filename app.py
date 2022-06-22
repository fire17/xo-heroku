# https://github.com/fire17/xo-heroku/edit/main/app.py

from xo import *
from flask import Flask

app = Flask(__name__)

@app.route('/<path:text>')
def my_view_func(text):
    if text.startswith("await/"):
        if len(text.split("/")[1])>0:
            key = text.split("/")[1]
            if xo.wait[key].value() == None:
                xo.wait[key] = "awaiting "+key+"..."
                xo.wait[key].done = False
            if len(text.split("/")) > 2 and len(text.split("/")[2])>0:
                value = text.split("/")[2]
                if len(text.split("/")) > 3 and len(text.split("/")[3])>0:
                    msg = text.split("/")[3]
                    xo.wait[key] = msg
                if "1" in value or "true" in value.lower():
                    xo.wait[key].done = True
                elif "0" in value or "false" in value.lower():
                    xo.wait[key].done = False
            res = xo.wait[key].done.value() == True
            return "@"+res+str(xo.wait[key].value())+"@@@"
    return "@1"+text+"!!!"
@app.route('/')
def hello():
    return 'Hello, World!'
