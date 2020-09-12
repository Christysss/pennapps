from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
# import API.flaskAPIs as api
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
app.config['MONGO_DBNAME'] = 'Pennapps'
app.config['MONGO_URI'] = "mongodb+srv://Pennapps:pennapps123@penapps.itvhn.gcp.mongodb.net/Pennapps?retryWrites=true&w=majority"
mongo = PyMongo(app)


# endpoint for rendering the calender template initially
@app.route('/getcalender', methods=['GET'])
def get_calender():
    event = mongo.db.calendar
    events = event.find()

    return jsonify(events)


# endpoint for fetching data for particular event by id of the event
# GET request
# Will return JSON data for one specific event

@app.route('/fetchevent', methods=['GET'])
def fetch_event():
    req_id = request.json['id']
    event = mongo.db.calendar
    event_select = event.find_one({'_id': req_id})
    return jsonify(event_select)


# endpoint for deleting an event
# event_id will be passed to the method.
# DELETE request
# Will return JSON data with success message

@app.route('/deleteevent', methods=['DELETE'])
def delete_event():
    req_id = request.json['id']
    event = mongo.db.calendar
    event_select = event.delete_one({'_id': req_id})
    return {"status": "success"}


# Create an event
# Time slots will be passed to the method
# Post request
# return success message

@app.route('/createevent', methods=['POST'])
def create_event():
    event = mongo.db.calendar
    event_name = request.json['event_name']
    startTime = request.json['startTime']
    endTime = request.json['endTime']

    event_id = event.insert({"event": event_name, "startTime": startTime, "endTime": endTime})

    return {"status": "success"}


# Update an event (Confusion: before than we need to make fetch request)
# event id will be passed
# POST request
# Return success message

@app.route('/updateevent', methods=['POST'])
def update_event():
    event = mongo.db.calendar
    req_id = request.json['id']

    # event.find_one_and_update({"_id" : req_id}, )

    return ""


# Graphapi
@app.route('/getdata', methods=['GET'])
def get_data():
    graph = mongo.db.graph
    graph_data = graph.find()
    return jsonify(graph_data)


# Todoapi

@app.route('/gettodos', methods=['GET'])
def get_todos():

    todo = mongo.db.todo
    todo_data = todo.find()
    return jsonify(todo_data)


# endpoint for adding to-do item.
# POST Request
# Send JSON success message back to caller

@app.route('/addtodo', methods=['GET'])
def add_todo():
    todo = mongo.db.todo

    req_data = request.json["task"]

    todo_id = todo.insert({"task" : req_data, "completed": False})

    return jsonify({"status":"success"})


# endpoint for removing an item from to-do list
# and add it to the achieved task
# Two possibilities : i) remove completely or ii) achieved task
# Boolean will be passed to method
# Send JSON response

@app.route('/removetodo', methods=['GET'])
def remove_todo():
    todo = mongo.db.todo

    completion = request.json["isCompleted"]
    task_name = request.json["task"]
    remove = request.json["remove"]

    if(remove == True):
        todo.delete_one({"task":task_name})
    else:
        todo.find_one_and_update({"task":task_name}, {"completion": completion})

    return jsonify({"status": "success"})


# endpoint for editing todo item
# POST request
# Get data and update the data

@app.route('/edittodo', methods=['GET'])
def edit_todo():
    todo = mongo.db.todo
    task_id = request.json["id"]
    task_name = request.json["task_name"]
    todo.find_one_and_update({"_id": task_id}, {"task": task_name})

    return jsonify({"status": "success"})



# Transcripts






# endpoint for rendering the transcript element initially
# GET Request
# Student ID will be passed to method and it will fetch all subects
#    taken by student and return it to caller
# return JSON response

@app.route('/getsubjects', methods=['GET'])
def get_subjects():
    return ""

# endpoint for fetching all the transcripts and required data for specific subject
# GET Request
# subject ID will be passed to the method
# return JSON response

# eg: details contain: video URL for the lecture, transcript URL (or text), Summary URL (or text)

@app.route('/gettranscripts', methods=['GET'])
def get_transcripts():
    return ""

















if __name__ == '__main__':
    app.run()
