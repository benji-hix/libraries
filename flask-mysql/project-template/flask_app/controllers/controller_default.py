from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_#* link model


@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('index.html')
