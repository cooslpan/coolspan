from flask import render_template
from . import  authblue
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from  ..models import  User
from .forms import LoginForm
from .forms import RegistrationForm
from .. import db,session
@authblue.route('/login', methods=['GET', 'POST'])


def login():
     form = LoginForm()
     if form.validate_on_submit():
         user = User.query.filter_by(email=form.email.data).first()
         if user is not None and user.verify_password(form.password.data):
             login_user(user, form.remember_me.data)
             next = request.args.get('next')
             if next is None or not next.startswith('/'):
                 next = url_for('main.index')
             return redirect(next)
         flash('Invalid username or password.')
     return render_template('auth/login.html', form=form)

@authblue.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        session.add(user)
        session.commit()
        token = user.generate_confirmation_token()
        session.close()
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/email/confirm', user=user, token=token)
        #flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)