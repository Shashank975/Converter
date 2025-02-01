# PDF Upload and Convert API

This is a simple **Flask API** that allows users to upload PDF files, and then convert the first page of the uploaded PDF into an image (PNG format). It uses `PyMuPDF` (fitz) to handle PDF to image conversion.

## Features
- **Upload PDF files** via a RESTful API.
- **Convert the first page of the uploaded PDF** into a PNG image.
- **Temporary file storage** on Render’s ephemeral file system (files are deleted after app restarts).
  
## Technology Stack
- **Backend:** Python, Flask
- **PDF Processing:** PyMuPDF (fitz)
- **Storage:** Temporary file system (ephemeral storage on Render)

## Installation

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
https://github.com/Shashank975/Converter.git

