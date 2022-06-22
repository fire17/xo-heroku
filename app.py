# https://github.com/fire17/xo-heroku/edit/main/app.py

from xo import *
from flask import Flask

app = Flask(__name__)

@app.route('/<path:text>')
def my_view_func(text):
    print("text :::",text)
    if text.startswith("await/"):
        if len(text.split("/")[1])>0:
            key = text.split("/")[1]
            print("key :::",key)
            if xo.wait[key].value() == None:
                xo.wait[key] = "awaiting "+key+"..."
                xo.wait[key].done = False
            if len(text.split("/")) > 2 and len(text.split("/")[2])>0:
                value = text.split("/")[2]
                print("value :::",value)
                if len(text.split("/")) > 3 and len(text.split("/")[3])>0:
                    msg = text.split("/")[3]
                    print("value :::",msg)
                    xo.wait[key] = msg
                if "1" in value or "true" in value.lower():
                    xo.wait[key].done = True
                elif "0" in value or "false" in value.lower():
                    xo.wait[key].done = False
            res = "0"
            if xo.wait[key].done.value() == True:
                res = "1"
            final = "@"+res+str(xo.wait[key].value())
            print("value :::",msg)
            print()
            return final
    print()
    return "@1"+text+"!!!echo!!!"
    
@app.route('/')
def hello():
    return 'Hello, World!'
