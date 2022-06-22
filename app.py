from xo import *
from flask import Flask

app = Flask(__name__)

@app.route('/<path:text>')
def my_view_func(text):
    if text.startswith("await/"):
        if len(text.split("/")[1])>0:
            key = text.split("/")[1]
            if xo.await[key].value() == None:
                xo.await[key] = False
            if len(text.split("/")) > 2 and len(text.split("/")[2])>0:
                value = text.split("/")[2]
                if "1" in value or "true" in value.lower():
                    xo.await[key] = True
                else:
                    xo.await[key] = False
    return "!!!"+str(xo.await[key].value())+"!!!"
  
@app.route('/')
def hello():
    return 'Hello, World!'
