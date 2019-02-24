import os
from flask import render_template, flash, redirect, request, url_for, send_file
from werkzeug.urls import url_parse
from werkzeug import secure_filename
from app import app, db
from app.forms import AcrolistForm
from acrolist import searcher

UPLOAD_PATH = '/home/rai/projects/di_apps/uploads/'

@app.route('/', methods=['GET', 'POST'])
def acrolist():
    form = AcrolistForm()
    if form.doc.data:
#        filename = secure_filename(form.doc.data.filename)
#        form.doc.data.save('uploads/' + filename) 
        use_parens = form.use_parens.data
        acronyms = searcher(form.doc.data)        
        f = open('output.txt','w')
        for i in acronyms:
            f.write(str(acronyms[1]) + ' ' + str(acronyms[2])+'\n')
        return send_file(f)
    return render_template('acrolist.html', form=form)
