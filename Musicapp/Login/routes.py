# from flask import render_template, url_for, flash, redirect, request, Blueprint
# from flask_login import login_user, current_user, logout_user

# from Musicapp import bcrypt
# from Musicapp.forms import UserSignupForm, LoginForm
# from Musicapp.models import insert_user, select_user, search_songs_by_artist, search_songs_by_genre, search_songs_by_title


# Login = Blueprint('Login', __name__)

# @Login.route("/")
# @Login.route("/home")
# def home():
#     if request.method == 'POST':
#         query = request.form['query']
#         search_type = request.form['search_type']
#         return redirect(url_for('Login.search', query=query, search_type=search_type))
#     return render_template('home.html')

# @Login.route("/about")
# def about():
#     return render_template('about.html')

# @Login.route("/register", methods=['GET', 'POST'])
# def register():
#     form = UserSignupForm()
#     if form.validate_on_submit():
#         insert_user(form.username.data, form.password.data)
#         flash('Your account has been created!', 'success')
#         return redirect(url_for('Login.login'))
#     return render_template('register.html', title='Register', form=form)


# @Login.route("/login", methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('Login.home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = select_user(form.user_name.data)
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=True)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('Login.home'))
#     return render_template('login.html', form=form)



# @Login.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('Login.login'))


# @Login.route('/search', methods=['GET', 'POST'])
# def search():
#     query = request.args.get('query')
#     search_type = request.args.get('search_type')
    
#     if search_type == 'song':
#         result = search_songs_by_title(query)
#     elif search_type == 'artist':
#         result = search_songs_by_artist(query)
#     elif search_type == 'genre':
#         result = search_songs_by_genre(query)
#     else:
#         return render_template('search.html', error='Invalid')
    
#     return render_template('search.html', results=result)
