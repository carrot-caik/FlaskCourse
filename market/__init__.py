from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '822160a8e44d878c44e88f44'
app.config['SESSION_COOKIE_SECURE'] = False
app.config['WTF_CSRF_SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

from market import routes