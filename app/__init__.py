from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_simplelogin import SimpleLogin, get_username, login_required
from app import users
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['NEO4J_USER'] = os.environ['NEO4J_USER']
app.config['NEO4J_PASSWORD'] = os.environ['NEO4J_PASSWORD']


SimpleLogin(app, login_checker=users.is_valid_user)
bootstrap = Bootstrap(app)
from app import routes
