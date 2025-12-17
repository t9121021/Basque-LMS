from flask import render_template, Blueprint, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app import db


auth = Blueprint('auth', __name__, template_folder ='templates')


# http://127.0.0.1:5000

@auth.route('/login', methods =['GET'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth.route('/login', methods = ["POST"])
def login_post():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Not implemented', 'info')
        return redirect(url_for('auth.login'))

    flash('Invalid form data', 'danger')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return render_template('auth/register.html', form=form)
        
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            password=hashed_password,
            role=form.role.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
    
@auth.route('/logout')
def logout():
     flash('Not implemented', 'info')
     return redirect(url_for('auth.login'))


