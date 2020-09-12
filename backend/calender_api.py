from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
# import API.flaskAPIs as api
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
CORS(app)
app.config['MONGO_DBNAME'] = 'Pennapps'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# endpoint for rendering the calender template initially
@app.route('/getcalender', methods=['GET'])
def get_calender():
    return ""

# endpoint for fetching data for particular event by id of the event
# GET request
# Will return JSON data for one specific event

@app.route('/fetchevent', methods=['GET'])
def fetch_event():
    return ""

# endpoint for deleting an event 
# event_id will be passed to the method.
# DELETE request
# Will return JSON data with success message

@app.route('/deleteevent', methods=['DELETE'])
def delete_event():
    return ""

# Create an event
# Time slots will be passed to the method
# Post request
# return success message

@app.route('/createevent', methods=['POST'])
def create_event():
    # star = mongo.db.stars
    # # name = request.json['name']
    # # distance = request.json['distance']
    # star_id = star.insert({'name': "name", 'distance': "distance"})
    # new_star = star.find_one({'_id': star_id})
    # output = {'name': new_star['name'], 'distance': new_star['distance']}
    # # return jsonify({'result': output})
    return ""

# Update an event (Confusion: before than we need to make fetch request)
# event id will be passed
# POST request
# Return success message

@app.route('/updateevent', methods=['POST'])
def update_event():
    return ""





if __name__ == '__main__':
    app.run()














