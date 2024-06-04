from flask import render_template, redirect, url_for, request,Blueprint
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import pandas as pd

Login = Blueprint('Login', __name__)

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# # Database configuration
# db_config = {
#     'dbname': 'your_db',
#     'user': 'your_user',
#     'host': 'localhost',
#     'password': 'your_password'
# }

# conn = psycopg2.connect(**db_config)

# @login_manager.user_loader
# def load_user(user_id):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
#     user = cur.fetchone()
#     cur.close()
#     if user:
#         return User(user)
#     return None

# class User(UserMixin):
#     def __init__(self, user):
#         self.id = user[0]
#         self.username = user[1]
#         self.password = user[2]

@Login.route('/createaccount', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            flash('Username already exists!')
        else:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            flash('Account created!')
            return redirect(url_for('home'))
        cur.close()
    return render_template('createaccount.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.check_password_hash(user[2], password):
            user_obj = User(user)
            login_user(user_obj)
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    cur = conn.cursor()
    cur.execute("SELECT * FROM songs ORDER BY RANDOM() LIMIT 10")
    songs = cur.fetchall()
    cur.close()
    return render_template('index.html', songs=songs)

@app.route('/songs/<int:song_id>')
@login_required
def song_page(song_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM songs WHERE song_id = %s", (song_id,))
    song = cur.fetchone()
    cur.close()
    if song:
        return render_template('song.html', song=song)
    else:
        abort(404)

