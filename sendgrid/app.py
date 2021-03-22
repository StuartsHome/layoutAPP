
from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "aquisition Type" : "SNMP",             
        "people": [                             # created an object that has a key inside which is a list
            {"name": "John", "age": 27},        # that list contains 2 objects
            {"name": "Sara", "age": 33}         # with the keys name and age

            ],
        "response": [
            {"responsecode": 4000000}
        ]
        }
    return jsonify(data)





"""
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
Original ENV file location: ${workspaceFolder}/.env
"""