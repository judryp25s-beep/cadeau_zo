from flask import Flask, jsonify, render_template
import requests
import os

API_KEY_CAT = 'live_3onHhrcUdVnJ11i76O5IIxMM86LwmCHMOXJJeTZkmcUKAClWuh33cZbKLBuHMKEh'
API_KEY_DOG = 'live_agmM8DP6IKVYH4FyesiEY8vE7ksZVPAtubtFTecDem2iqDMvUo7rTBiSa1at91bB'
API_URL_DOG = 'https://api.thedogapi.com/v1/images/search?limit=10'
API_URL_CAT = 'https://api.thecatapi.com/v1/images/search?limit=10'

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/dogs_images')
def get_dogs():
    headers = {"x-api-key": API_KEY_DOG}
    response = requests.get(API_URL_DOG, headers=headers)
    return jsonify(response.json())

@app.route('/cats_images')
def get_cats():
    headers = {"x-api-key": API_KEY_CAT}
    response = requests.get(API_URL_CAT, headers=headers)
    return jsonify(response.json())

@app.route('/dogs')
def dog():
    return render_template('dog.html')

@app.route('/cats')
def cat():
    return render_template('kitten.html')
