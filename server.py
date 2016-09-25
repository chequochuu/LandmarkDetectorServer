from flask import Flask, request, send_file
from oct2py import octave
import os
import numpy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/che/test/'

@app.route('/')
def hello():
    return """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="client_post" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        <p>%s</p>
        """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'], ))

@app.route('/files/<filename>')
def get_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/client_post', methods=['POST'])
def add_client_file():
    imgfile = request.files['file']
    if imgfile:
        filename = imgfile.filename
        imgfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Xử lý, tính toán, gọi MATLAB, ... ở đây
        octave.addpath("/home/che/Downloads/train")
        t = octave.thu()
        return str(t)
    return 'ERR'

if __name__ == '__main__':
    app.run()