from flask import Flask, send_from_directory
import sys
import os

# Prevent Python from writing .pyc files
sys.dont_write_bytecode = True

# Initialize Flask app
app = Flask(__name__)

# Import controllers and models
import controller.controller
import model.model

# Example route
@app.route('/hello')
def hello():
    return 'Hello, World!'

# Serve other static files (CSS, JS, Images)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
