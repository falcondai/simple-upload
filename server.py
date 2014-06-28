#!/usr/bin/python

import os, uuid

from flask import Flask, render_template, flash, request
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = 'secret'
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        files =  request.files.getlist('set')
        print files
        if len(files) < 1 or files[0].filename == '':
            flash('No files received?!')
        else:
            flash('%d files received successfully.' % len(files))
            for f in files:
                f.save(os.path.join('upload', uuid.uuid1().hex + '-' + secure_filename(f.filename)))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
