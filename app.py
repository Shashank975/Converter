from flask import Flask
app = Flask(__name__)
import sys
sys.dont_write_bytecode = True
import os 

@app.route('/')
def home():
    return 'Hello, World!'

import controller.controller 
import model.model