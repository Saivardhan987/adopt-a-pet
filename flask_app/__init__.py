from flask import Flask

app = Flask(__name__)

app.secret_key = "This is a secret"

app.config['UPLOAD_FOLDER'] = 'flask_app/static/form_data/'