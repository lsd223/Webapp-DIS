from flask import render_template, url_for, redirect, request, Blueprint
from Musicapp import app
from Musicapp.models import search_songs_by_title, search_songs_by_artist, search_songs_by_genre

Search = Blueprint('Login', __name__)

@Search.route('/', methods = ['GET','POST'])
def indexpage():
    '''Returns the landing page of the search engine web application'''
    if request.method == 'GET':
        return render_template('index.html')
    else:
        query = request.form['query']
        search_type = request.form['search_type']
        return redirect(url_for('results',query = query, search_type = search_type))

@Search.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form['query']
        search_type = request.form['search_type']
        
        if search_type == 'song':
            result = search_songs_by_title(query)
        elif search_type == 'artist':
            result = search_songs_by_artist(query)
        elif search_type == 'genre':
            result = search_songs_by_genre(query)
        else:
            return render_template('search.html', error = 'Invalid')
    return render_template('search.html', results = result)



