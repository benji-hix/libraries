# ---------------------------------------------------------------------------- #
#~                                    create                                    #
# ---------------------------------------------------------------------------- #
    
#`` -------------------------------- model file -------------------------------- #

# ---------------------------------- create ??? ---------------------------------- #
    @classmethod
    def create_???(cls, form):
        query = """
        INSERT INTO ????? ( ???, created_at, updated_at )
        VALUES ( %()s, NOW(), NOW() );
        """
        data = {
            '' : form[''],
   
        }
        return connectToMySQL(app_database).query_db(query, data)

#`` ------------------------------ controller file ----------------------------- #

# ---------------------------- submit new ??? ---------------------------- #
@app.route('/submit_???', methods=['POST'])
def submit_???():
    ???_model.Class?.create_???(request.form)
    redirect_url = '//' + str(session['user_id'])
    return redirect(redirect_url)


# ---------------------------------------------------------------------------- #
#~                                    delete                                    #
# ---------------------------------------------------------------------------- #

#`` -------------------------------- model file -------------------------------- #

# ------------------------------ delete ??? ------------------------------ #
    @classmethod
    def delete_???(cls, pk):
        query = """
        DELETE FROM ???
        WHERE id = %(???_id)s;
        """
        data = { '???_id' : pk }
        return connectToMySQL(app_database).query_db(query, data)

#`` -------------------------------- controller file -------------------------------- #

# ------------------------------ delete ??? ------------------------------ #
@app.route('/delete/<int:pk>')
def delete_???(pk):
    ???_model.Class?.delete_???(pk)
    redirect_url = '//' + str(session['user_id'])
    return redirect(redirect_url)


# ---------------------------------------------------------------------------- #
#~                                    update                                    #
# ---------------------------------------------------------------------------- #

#` -------------------------------- model file -------------------------------- #
# -------------------------------- update ??? -------------------------------- #
    @classmethod
    def update_???(cls, form, pk):
        query = """UPDATE ??? 
                SET ? = %()s, updated_at = NOW() 
                WHERE id = %(id)s;"""
        data = {
            'id' : form['form_id'],
            '' : form[''],
        }
        return connectToMySQL(app_database).query_db(query, data)

#`` ------------------------------ controller file ----------------------------- #
@app.route('/submit_update/<int:pk>', methods = ['POST'])
def ???_submit_update():
    use??? = model_???.Class?.update_???(request.form, pk)
    redirect_url = '//' + str(session['user_id'])
    return redirect(redirect_url)

# ---------------------------------------------------------------------------- #
#~                                     read                                    #
# ---------------------------------------------------------------------------- #


#* ------------------------------- single table ------------------------------- #


# ------------------------------- read all ??? ------------------------------- #
    @classmethod
    def read_all_???(cls):
        query = """SELECT * FROM ???;
        ORDER BY ???;
        """
        results = connectToMySQL(app_database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

# ------------------------------- read one ??? ------------------------------- #
    @classmethod
    def read_???(cls, pk):
        query = """SELECT * FROM ???
                WHERE id = %(id)s
                ORDER BY ???;"""
        data = {'id': pk}
        results = connectToMySQL(app_database).query_db(query, data)
        return cls(results[0])

# ------------------------ read one value? ----------------------- #
    @classmethod
    def read_???(cls):
        query = """
        SELECT count(???.id) AS ???_count FROM ???
        WHERE ???.???_id = %(???_id)s
        """
        data = { '???+id' : session['user_id'] }
        result = connectToMySQL(app_database).query_db(query, data)[0]
        return result


#* --------------------------------- self join -------------------------------- #

# -------------------------- read self-join -------------------------- #
    @classmethod
    def read_???(cls):
        query = """
        SELECT * FROM table1
        LEFT JOIN table2 on table1.id = table2.instance1_id
        LEFT JOIN table1 AS ? ON table2.?_id= ?.id
        WHERE table2.instance1_id = %(user_id)s
        """
        data = {'user_id' : session['user_id'] }
        return connectToMySQL(app_database).query_db(query, data)


# -------------------------------- one to many ------------------------------- #
    @classmethod
    def read_???_with_???( cls , pk ):
        query = """SELECT * 
                FROM table1?
                LEFT JOIN table2 on  table1.id= table2.instance1_id 
                WHERE table1.id = %(id)s;"""
        data = { 'id': pk }
        results = connectToMySQL(cls.database).query_db( query , data )
        
        instance1 = cls( results[0] ) #! 

        for row in results:
            if row['table2.id'] == None:
                break
            instance2_data = { #! match class constructor in opposite file 
                "id" : row["table2.id"],
                "" : row[""],
                "created_at" : row["table2.created_at"],
                "updated_at" : row["table2.updated_at"]
            }
            model_instance1.array_name.append( model_instance2.Class2?( instance2_data ) )

        return dojo