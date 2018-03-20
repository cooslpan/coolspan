from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import create_engine,Column, Integer, String,CHAR
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
from flask.ext.login import  UserMixin
from . import db, login_manager


class User(UserMixin,db):
   __tablename__='user'
   id = Column(Integer, primary_key=True)

   username = Column(CHAR(30))
   password_hash= Column(String(128))
   email = Column(String(64),unique=True,index=True)
   role_id = Column(Integer)

   @property
   def password(self):
       raise AttributeError('password is not readable attrbute')

   @password.setter
   def password(self,password):
       self.password_hash = generate_password_hash(password)

   def verify_password(self,password):
       return  check_password_hash(self.password_hash,password)
   def generate_confirmation_token(self, expiration=3600):
       s = Serializer(current_app.config['SECRET_KEY'], expiration)
       return s.dumps({'confirm': self.id}).decode('utf-8')
#登录
from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

