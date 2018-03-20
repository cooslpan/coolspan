
from flask import Flask,render_template
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view='auth.login'
import sys
import os

#PACKAGE_PARENT = '..'

#sys.path.append(PACKAGE_PARENT)
import os,sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column, Integer, String,CHAR
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/myblog", max_overflow=5)
db = declarative_base()
DB_Session = sessionmaker(bind=engine)
session = DB_Session()


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
print(parentdir)
print(sys.path)


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'xxx'
    bootstrap.init_app(app)
    from .auth import authblue as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)
    return app

