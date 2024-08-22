from flask import request, jsonify
from app import app
from app.storage import upload_file_to_s3, get_file_from_s3

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    upload_file_to_s3(file, filename)
    return jsonify({'message': 'File uploaded successfully!'})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_data = get_file_from_s3(filename)
    return file_data, 200, {'Content-Type': 'application/octet-stream'}
