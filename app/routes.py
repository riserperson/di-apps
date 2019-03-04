import os
from flask import render_template, flash, redirect, request, url_for, send_file
from werkzeug.urls import url_parse
from werkzeug import secure_filename
from app import app, db
from app.forms import AcrolistForm
from acrolist import searcher
import docx2txt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acrolist', methods=['GET', 'POST'])
def acrolist():
    if not os.path.exists(app.root_path + '/tmp/'):
        os.mkdir(app.root_path + '/tmp/')
    if os.path.isfile(app.root_path + '/tmp/output.txt'):
        os.remove(app.root_path + '/tmp/output.txt')

    form = AcrolistForm()
    if form.doc.data:
        input_file = open(app.root_path + '/tmp/input.txt','w+x')
        if form.doc.data.filename[-4:] == 'docx':
            text = docx2txt.process(form.doc.data)
        else:
            text = form.doc.data
        input_file.write(str(text))
        input_file.close()
        acronyms = searcher(input_file)
        f = open(app.root_path + '/tmp/output.txt','w+x')
        for x in acronyms:
            f.write(str(x)+'\n')
        f.close()
        return send_file(app.root_path + '/tmp/output.txt', as_attachment=True, attachment_filename='output.txt', mimetype='text/plain')
    return render_template('acrolist.html', form=form)
