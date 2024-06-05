from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user

from MusicApp import app, conn, bcrypt
from MusicApp.forms import UserSignupForm, LoginForm
from MusicApp.models import insert_user, select_user


Login = Blueprint('Login', __name__)

@Login.route("/")
@Login.route("/home")
def home():
    return render_template('home.html')

@Login.route("/about")
def about():
    return render_template('about.html')

@Login.route("/register", methods=['GET', 'POST'])
def register():
    form = UserSignupForm()
    if form.validate_on_submit():
        
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)


@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = select_user(form.user_name.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
    return render_template('pages/login.html', form=form)



@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.login'))

