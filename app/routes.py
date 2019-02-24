import os
from flask import render_template, flash, redirect, request, url_for, send_file
from werkzeug.urls import url_parse
from werkzeug import secure_filename
from app import app, db
from app.forms import AcrolistForm
from acrolist import searcher

UPLOAD_PATH = '/home/rai/projects/di_apps/uploads/'
if not os.path.exists('tmp'):
    os.mkdir('tmp')

@app.route('/', methods=['GET', 'POST'])
def acrolist():
    form = AcrolistForm()
    if form.doc.data:
        use_parens = form.use_parens.data
        acronyms = searcher(form.doc.data)        
        f = open('tmp/output.txt','w+')
        for x, y in acronyms.items():
            f.write(str(x) + ' ' + str(y)+'\n')
        return send_file(f, attachment_filename='output.txt', as_attachment=True, mimetype='text/plain')
    return render_template('acrolist.html', form=form)
