from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_user, model_#*CHANGE


@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('access.html') #*CHANGE


#~ ------------- submit register attempt, validate, create, log in ------------ #
@app.route('/submit-register', methods = ['POST'])
def submit_register():

    if not model_user.User.validate_register(request.form): return redirect('/')  #| validate
    session['user_id'] = model_user.User.register(request.form)  #| register + store id

    return redirect('/recipes') #*CHANGE


#~ ------------------ submit log-in attempt, validate, log in ----------------- #
@app.route('/submit-login', methods=['POST'])
def submit_login():

    if not model_user.User.validate_login(request.form): return redirect('/')  #| validate + store user_id

    return redirect('/recipes') #*CHANGE


#~ ---------------------------------- log out --------------------------------- #
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')

#* ------------------------ view single user's ??? ------------------------ #
@app.route('/???/user/<int:pk>') #*CHANGE
def user_(pk): #*CHANGE
    return render_template('user-.html', user=model_user.User.user_with_(pk))#*CHANGE
    