from app import app
from flask import Flask, request
import sys
sys.dont_write_bytecode = True
import os 
import fitz

#Here You will gonna Write your Logic Of the Code.
class Uploading():

    def __init__(self):
        self.upload_folder = 'uploads'
        self.download_folder = 'output'

                # Make sure both folders exist
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)



    def Convert(self,file):
        
        # Load the PDF
        pdf_path = os.path.join(self.upload_folder, file.filename)
        file.save(pdf_path)
        doc = fitz.open(pdf_path)
            
        # Convert the first page to an image
        page = doc.load_page(0)  # 0 refers to the first page
        pix = page.get_pixmap()
            
        # Save the image to the download folder
        output_filename = os.path.join(self.download_folder, f"{os.path.splitext(file.filename)[0]}.png")
        pix.save(output_filename)
        return {"Message": f"File converted and saved as: {pdf_path}"}






































    # def upload(self):
    #     return "Everything  is Setup"

    # #This function is fofr the file Uploading.
    # def file_upload(self, filepath):
    #     return f"File uploaded successfully: {filepath}"

    # def file_convert(self):
    #     return "Let write the code for the Conversion"