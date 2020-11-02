from flask import Flask
from flask import request
import requests
import json
import os

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello Wolrd!"

@app.route('/covid_data/<country>', methods=('get', 'post'))
def covidData(country):
    countryResult = None
    response = requests.get('https://api.covid19api.com/summary')
    if response.status_code == 200:
        res = json.loads(response.text)
        if country.upper() == 'ALL':
            print('test')
            countryResult = res
        if country.upper() != 'ALL':
            for count in range(len(res["Countries"])):
                if res["Countries"][count]["CountryCode"] == country.upper():
                    countryResult = res["Countries"][count]
            if countryResult is None:
                countryResult = 'Country not found'
        return countryResult

@app.errorhandler(404) 
def not_found(e):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'no_reponse.txt')
    with open(my_file, 'r') as file:
        data = file.read()
    return data

if __name__=='__main__':
    app.run(debug=True)