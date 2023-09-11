from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Model: #*
    database = 'DATABASE_NAME_HERE' #*CHANGE

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self. = data[''] #*CHANGE
        self. = data[''] #*CHANGE
        self. = data[''] #*CHANGE
        self.join = []

# --------------------------------- validate --------------------------------- #
    @staticmethod
    def validate_form(form): #* CHANGE
        is_valid = True
        query = "SELECT * FROM ___ WHERE ___ = %()s" #*insert parameter to check for unique
        unique_fail = connectToMySQL('database').query_db(query, form)

        if not email_regex.match(email['form_email']):
            flash('Invalid email address')
            is_valid = False
        elif unique_fail:
            flash('____ already exists in database') #* insert paramter to check for unique
            is_valid = False
        elif condition: #* CHANGE
            flash('')
            is_valid = False

        return is_valid 

# --------------------------------- read all --------------------------------- #
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM ___" #*CHANGE
        results = connectToMySQL(app_database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all


# --------------------------------- read one --------------------------------- #
    @classmethod
    def read(cls, pk):
        query = """SELECT * FROM ____ #*CHANGE
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(app_database).query_db(query, data)
        return results[0]


# ---------------------------------- create ---------------------------------- #
    @classmethod
    def create(cls, data):
        query = """INSERT INTO __ ( __, created_at, updated_at ) #*CHANGE
                VALUES ( %()s, NOW(), NOW() );""" #*CHANGE
        return connectToMySQL(app_database).query_db(query, data)


# ---------------------------------- update ---------------------------------- #
    @classmethod
    def update(cls, data):
        query = """UPDATE ___ #*CHANGE 
                SET ___ = %()s, updated_at = NOW() #*CHANGE
                WHERE id = %(form_id)s;"""
        return connectToMySQL(app_database).query_db(query, data)


# ---------------------------------- delete -----------------------------------#
    @classmethod
    def delete(cls, pk):
        query = """DELETE FROM #*CHANGE
                WHERE id = %(id)s;"""
        data = {"id": pk}
        return connectToMySQL(app_database).query_db(query, data)

# ----------------------------------- join ----------------------------------- #
    @classmethod
    def ALPHA_with_BETA(cls, pk):
        query ="""SELECT * FROM alphas
                LEFT JOIN connector
                ON alphas.id = connector.alpha_id
                LEFT JOIN betas
                ON connector.beta_id = betas.id
                WHERE alphas.id = %(id)s"""
        data = { 'id': pk }
        results = connectToMySQL(app_database).query_db(query, data)

        alpha = cls(results[0])

        for row in results:
            if row['betas.id'] == None:
                break
            beta_data = {
                'id' : row['beta.id'],
                'created_at' : row['betass.created_at'],
                'updated_at' : row['betas.created_at']
            }
            alpha.join.append( beta.Beta(beta_data) )
            
        return alpha