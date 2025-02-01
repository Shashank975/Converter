# from flask import Flask
# app = Flask(__name__)

# import sys
# sys.dont_write_bytecode = True


# import controller.controller 
# import model.model
# import os 


from flask import Flask, send_from_directory
import os

app = Flask(__name__)

import sys
sys.dont_write_bytecode = True

import controller.controller
import model.model
import os

# Example route
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
