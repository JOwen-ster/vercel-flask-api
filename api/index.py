from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify('Haiii :3')

@app.route('/about')
def about():
    return jsonify('About')