# coding=utf8
import os
from flask import render_template, flash, redirect, request, url_for, send_file
from werkzeug.urls import url_parse
from werkzeug import secure_filename
from app import app, db
from app.forms import AcrolistForm
from acrolist import searcher
import docx2txt
import codecs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acrolist', methods=['GET', 'POST'])
def acrolist():
    if not os.path.exists(app.root_path + '/tmp/'):
        os.mkdir(app.root_path + '/tmp/')
    if os.path.isfile(app.root_path + '/tmp/of.txt'):
        os.remove(app.root_path + '/tmp/of.txt')

    form = AcrolistForm()
    if form.doc.data:
        if form.doc.data.filename[-4:] == 'docx' or form.doc.data.filename[-3] =='doc':
            text = docx2txt.process(form.doc.data).encode('utf8')
        else:
            flash('Unsupported file format')
            return render_template('acrolist.html', form=form)
        acronyms = searcher(text)
        f = open(app.root_path + '/tmp/of.txt','wb+x')
        f.write('\r\n'.join(acronyms))
        f.close()
        return send_file(app.root_path + '/tmp/of.txt', as_attachment=True, attachment_filename='output.txt', mimetype='text/plain')
    return render_template('acrolist.html', form=form)
