#!/usr/bin/env python
# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from flask import  Flask
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= "mysql+mysqldb://root:root@127.0.0.1:3306/myblog"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#-------------------------------------------
#可以正常使用的程序
# from sqlalchemy import create_engine
# engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/myblog", max_overflow=5)
#
# engine.execute(
#     "INSERT INTO User VALUES ('1', 'v1')"
#  )
#------------------------------------------
from sqlalchemy import create_engine,Column, Integer, String,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash,check_password_hash

engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/myblog", max_overflow=5)
Base = declarative_base()
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
# from sqlalchemy import Column
# from sqlalchemy.types import CHAR, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
#from random import randint
#from sqlalchemy import ForeignKey
#db = declarative_base(
class User(Base):
   __tablename__='user'
   ID = Column(Integer, primary_key=True)
   Name = Column(CHAR(30))
   email=co
   password_hash= Column(String(128))

   @property
   def password(self):
       raise AttributeError('password is not readable attrbute')

   @password.setter
   def password(self,password):
       self.password_hash = generate_password_hash(password)

   def verify_password(self,password):
       return  check_password_hash(self.password_hash,password)
print("1")
stu = User(Name = 'a')
stu.password = 'cat'
session.add(stu)
session.commit()
# 关闭session:
session.close()
print("2")