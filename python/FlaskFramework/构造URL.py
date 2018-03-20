#-*- coding:utf-8 –*-
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass
2
with app.test_request_context():
    print(url_for('index'))# 调用index函数
    print(url_for('login'))# 调用login函数
    print(url_for('login', next='/',gz='gz'))
    print(url_for('profile', username='John Doe'))