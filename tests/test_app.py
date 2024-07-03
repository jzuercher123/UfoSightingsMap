# Conduct tests for app.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('deprecated_index.html')

# API
@app.route('/api')
def api():
    return "This is the API endpoint"


