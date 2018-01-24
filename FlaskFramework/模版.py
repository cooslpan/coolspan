#-*- coding:utf-8 –*-
from flask import render_template
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # fake user
    return render_template("index.html",
        title = 'Home',
        user = user) #这里模块里的第一个user指的是html里面的变量user，而第二个user指的是函数index里面的变量user
if __name__ == '__main__':
    app.run()