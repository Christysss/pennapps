from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import API.flaskAPIs as api

app = Flask(__name__)
CORS(app)

# endpoint for rendering the graphs initially
# GET Request

@app.route('/getdata', methods=['GET'])
def get_data():
    return ""

# More methods will be added as per the interactions.