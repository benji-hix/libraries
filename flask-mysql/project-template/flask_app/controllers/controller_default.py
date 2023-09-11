from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model #*link model*



@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------------- create ---------------------------------- #
@app.route('/submit_', methods = ['POST'])
#*insert routes, Class
def submit_default():
    if not model.Model.validate_form(request.form):
        return redirect('/')
    Model.create(request.form)
    return redirect('/DEFAULTS')

# ----------------------------------- read ----------------------------------- #
@app.route('/DEFAULTS') #* CHANGE
#*insert routes, Class
def all_defaults():
    all_defaults = DEFAULT.read_all()
    return render_template('index.html', all_defaults = all_defaults)

@app.route('/DEFAULTS/<int:pk>')
def one_default(pk):
    model = model.Model.read(pk)
    return render_template('new_index.html', model = model)

# ---------------------------------- update ---------------------------------- #
@app.route('/submit_update', methods = ['POST'])
def submit_update():
    model = model.Model.update(request.form)
    return redirect('/DEFAULTS/' + str(request.form['form_id']))


# ---------------------------------- delete ---------------------------------- #
@app.route('/DEFAULTS/<int:pk>/delete')
def delete_default(pk):
    model.Model.delete(pk)
    return redirect('/DEFAULTS')

@app.route('/DEFAULT')
def read_join(pk):
    alpha = alpha.Alpha.read(pk)
    join_data = alpha.Alpha.ALPHA_with_BETA(pk)
    return render_template('dojos.html', alpha=alpha, join_data=join_data)