from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import API.flaskAPIs as api

app = Flask(__name__)
CORS(app)

# endpoint for rendering the to-do template initially
# GET Request

@app.route('/gettodos', methods=['GET'])
def get_todos():
    return ""

# endpoint for adding to-do item.
# POST Request
# Send JSON success message back to caller

@app.route('/addtodo', methods=['GET'])
def add_todo():
    return ""

# endpoint for removing an item from to-do list
# and add it to the achieved task
# Two possibilities : i) remove completely or ii) achieved task
# Boolean will be passed to method
# Send JSON response

@app.route('/removetodo', methods=['GET'])
def remove_todo():
    return ""

# endpoint for editing todo item
# POST request
# Get data and update the data 

@app.route('/edittodo', methods=['GET'])
def edit_todo():
    return ""