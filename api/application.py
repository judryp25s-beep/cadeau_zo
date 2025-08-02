from flask import Flask, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_CAT = os.getenv("CAT_API_KEY")
API_KEY_DOG = os.getenv("DOG_API_KEY")
API_URL_DOG = "https://api.thedogapi.com/v1/images/search?limit=10"

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/dogs')
def get_dogs():
    headers = {"x-api-key": API_KEY_DOG}
    response = requests.get(API_URL_DOG, headers=headers)
    return jsonify(response.json())


@app.route('/cats')
def get_dogs():
    headers = {"x-api-key": API_KEY_CAT}
    response = requests.get(API_URL_CAT, headers=headers)
    return jsonify(response.json())
