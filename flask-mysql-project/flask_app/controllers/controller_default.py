from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model #*link model*

@app.route('/DEFAULTS')
#*insert routes, Class
def index():

    all_defaults = DEFAULT.get_all()
    return render_template('index.html', all_defaults = all_defaults)


@app.route('/submit_new_default', methods = ['POST'])
#*insert routes, Class
def submit_default():
    Model.create(request.form)
    return redirect('/DEFAULTS')


