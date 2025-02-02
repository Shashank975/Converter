from flask import Flask, send_from_directory
import os
import sys
from flask_cors import CORS  # Import CORS

sys.dont_write_bytecode = True
# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)
# Import controllers and models
import controller.controller
import model.model

# Example route
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
