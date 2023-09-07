from flask_app.config.mysqlconnection import connectToMySQL

class Model: #*
    database = 'DATABASE_NAME_HERE' #*CHANGE

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self. = data[''] #*CHANGE

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM ___" #*CHANGE
        results = connectToMySQL(cls.database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

    @classmethod
    def read(cls, pk):
        query = """SELECT * FROM ____ #*CHANGE
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results[0]

    @classmethod
    def create(cls, data):
        query = """INSERT INTO __ ( __, created_at, updated_at ) #*CHANGE
                VALUES ( %()s, NOW(), NOW() );""" #*CHANGE
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """UPDATE ___ #*CHANGE 
                SET ___ = %()s, updated_at = NOW() #*CHANGE
                WHERE id = %(form_id)s;"""
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def delete(cls, pk):
        query = """DELETE FROM #*CHANGE
                WHERE id = %(id)s;"""
        data = {"id": pk}
        return connectToMySQL(cls.database).query_db(query, data)