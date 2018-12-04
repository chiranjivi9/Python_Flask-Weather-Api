from flask import Flask, jsonify, request, render_template
# export FLASK_DEBUG=1
import random
import requests
from quotes import allQuotes


app = Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/api/quotes')
def funnyQuotes():
    quotes = allQuotes()
    numOfQuotes = len(quotes)
    selectedQuote = quotes[random.randint(0, numOfQuotes - 1)]
    return jsonify(selectedQuote)

@app.route("/api/weather", methods=['POST'])
def weather():
    zipcode = request.form['zip']
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=08718eeb31e4585f7ff1f98e7480594f')
    jsonObject = r.json()
    # tempMaxMin = jsonObject["main"]["temp_min"]["temp_max"]
    tempKelvin = float(jsonObject["main"]["temp"])
    tempFahrenheit = (tempKelvin - 273.15) * 1.8 + 32
    return render_template('weather.html', temp = tempFahrenheit)
    # return jsonObject
    # return render_template('weather.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
