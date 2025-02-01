from flask import Flask
app = Flask(__name__)

import sys
sys.dont_write_bytecode = True


import controller.controller 
import model.model
import os 