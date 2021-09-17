import requests
import json
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return ""



@app.route("/proxy")
def proxy():
    url = request.args.get('url')
    type = request.args.get('type')
    if type == "vk":
        r = requests.get("https://api.vk.com/method/" + url).text
        return r

    r = requests.get(url).text
    return r




if __name__ == "__main__":
    app.run(debug=False)