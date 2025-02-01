from app import app
from model.model import Uploading
from flask import Flask, request,jsonify
import sys
sys.dont_write_bytecode = True
import os 

#Here You will calling the Function 
obj = Uploading()


@app.route("/api/covert", methods=["POST"])
def convertingApi():
    if 'pdffile' not in request.files:
        return jsonify({"Error": "No file part"})
    
    file = request.files['pdffile']
    if file.filename == '':
        return jsonify({"Error": "No selected file"})
    
    # Convert the uploaded file
    convert_response = obj.Convert(file)
    return jsonify(convert_response)














# #This route is used for the File Uploading
# @app.route("/api/fileUploading/flup", methods=["POST"])
# def uploadingApi():
#     file = request.files.get('flup')  # Ensures file is not None  
#     finalfilepath = f"Uploads/{file.filename}"
#     temp = file.save(finalfilepath)
#     return obj.file_upload(finalfilepath)

# @app.route("/api/convert", methods=["Get"])
# def convertApi():
#     return obj.file_convert()