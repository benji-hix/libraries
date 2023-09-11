from flask import Flask

app = Flask(__name__)
app.secret_key = "DEFAULT"

app_database = 'DEFAULT' #*insert any app-wide database here*