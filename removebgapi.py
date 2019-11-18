from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import requests

app = Flask(__name__)
# Enable CORS
CORS(app)

@app.route("/removebg", methods=["POST"])
def removebgapi():
    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('jerry.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'RGhvvuPjKwbnceGfBPiJsrum'},
    )
    if response.status_code == requests.codes.ok:
            with open('heroku.jpg', 'wb') as out:
                out.write(response.content)
    else:
            print("Error:", response.status_code, response.text)

