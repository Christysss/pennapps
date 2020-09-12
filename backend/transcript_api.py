from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
# import API.flaskAPIs as api

app = Flask(__name__)
CORS(app)

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

