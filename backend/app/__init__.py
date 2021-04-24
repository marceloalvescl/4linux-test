from flask import Flask, session
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/test4linux'
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Esse import é realizado após o login_manager ser executado para evitar erro de circular import
from routes.routes import consume_public_apis_routes
app.register_blueprint(consume_public_apis_routes)
