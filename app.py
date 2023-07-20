from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/about')
def about():
    return 'This is a URL shortener'