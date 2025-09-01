from flask import Flask, render_template, url_for
from flask_login import LoginManager
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_toastr import Toastr

app = Flask(__name__)
toastr = Toastr()

app.config['DEBUG'] = True
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

toastr.init_app(app)

bcrypt = Bcrypt(app)

def db_connect():   
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
    if not db_uri:
        raise ValueError("SQLALCHEMY_BINDS not found in app config.")
    con = psycopg2.connect(db_uri)
    return con

with app.app_context():
    from aplikasi.controllers import login, register
    