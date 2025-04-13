from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Haiii :3'

@app.route('/about')
def about():
    return 'About'