from flask import flask

app = Flask(__name__)
app.secret_key = "DEFAULT"

#*insert any app-wide database here*