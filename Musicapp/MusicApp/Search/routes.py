from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint
from MusicApp import app, conn, bcrypt
from MusicApp.models import search_songs_by_title, search_songs_by_artist, search_songs_by_genre

# app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def indexpage():
    '''Returns the landing page of the search engine web application'''
    if request.method == 'GET':
        return render_template('index.html')
    else:
        query = request.form['query']
        search_type = request.form['search_type']
        return redirect(url_for('results',query = query, search_type = search_type))

@app.route('/search', methods=['GET', 'POST'])
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




