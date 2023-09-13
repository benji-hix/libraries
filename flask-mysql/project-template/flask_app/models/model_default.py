from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app_database, app, bcrypt
from flask_app.models import model_#*CHANGE
from flask import flash, session


class Model: #*

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self. = data[''] #*CHANGE
        self._list = [] #*for -many relationships


#* ------------------------------ validate recipe ----------------------------- #
    @staticmethod
    def validate_recipe(form):

        is_valid = True

        #* blank forms 
        if len(form['form_']) < 1: #*CHANGE
            flash('Please complete DEFAULT field', '') #*CHANGE
            is_valid = False

        #| radio buttons
        if not (form.get('form_')): #*CHANGE
            flash('Please ', '') #*CHANGE
            is_valid = False
        #* required number of characters entered
        if len(form['form_']) < 3:
            flash('DEFAULT must be at least DEFAULT characters in length', '')#*CHANGE
            is_valid = False

        
        return is_valid
