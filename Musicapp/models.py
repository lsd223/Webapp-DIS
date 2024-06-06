# write all your SQL queries in this file.

from Musicapp import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql

@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    schema = 'users'
    id = 'user_id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema), sql.Identifier(id))

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return User(cur.fetchone())
    else:
        return None

class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.id = user_data[0]
        self.username = user_data[1]
        self.password = user_data[2]
        self.role = "user"

    def get_id(self):
       return (self.id)

#Insert
def insert_user(username, password):
    cur = conn.cursor()
    sql = """
    INSERT INTO users (username, password)
    VALUES (%s, %s)
    """
    cur.execute(sql, (username, password))
    conn.commit()
    cur.close()


#Select
def select_artist(name):
    cur = conn.cursor()
    sql = """
    SELECT * FROM artist WHERE name = %s
    """
    cur.execute(sql, (name))
    artists = cur.fetchall()
    cur.close()
    return artists

def select_song(title):
    cur = conn.cursor()
    sql = """
    SELECT * FROM song WHERE title = %s
    """
    cur.execute(sql, (title))
    songs = cur.fetchall()
    cur.close()
    return songs


def search_songs_by_title(title):
    cur = conn.cursor()
    sql = """
    SELECT songs.name, artist.name, songs.genre
    FROM songs
    JOIN artist ON songs.artist_id = artist.artist_id
    WHERE songs.name = %s
    """
    cur.execute(sql,(title,))
    results = cur.fetchall()
    cur.close()
    return [{'title': row[0], 'artist': row[1], 'genre': row[2]} for row in results]



def search_songs_by_artist(artist_name):
    cur = conn.cursor()
    sql = """
    SELECT songs.name, artist.name, songs.genre
    FROM songs
    JOIN artist ON songs.artist_id = artist.artist_id
    WHERE artist.name = %s
    """
    cur.execute(sql,(artist_name,))
    results = cur.fetchall()
    cur.close()
    return [{'title': row[0], 'artist': row[1], 'genre': row[2]} for row in results]

def search_songs_by_genre(genre):
    cur = conn.cursor()
    sql = """
    SELECT songs.name, artist.name, songs.genre
    FROM songs
    JOIN artist ON songs.artist_id = artist.artist_id
    WHERE songs.genre = %s
    """
    cur.execute(sql,(genre,))
    results = cur.fetchall()
    cur.close()
    return [{'title': row[0], 'artist': row[1], 'genre': row[2]} for row in results]
    

def select_user(username):
    cur = conn.cursor()
    sql = """
    SELECT * FROM users
    WHERE username = %s
    """
    cur.execute(sql, (username,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user


#Update
def update_password(user_id, new_password):
    cur = conn.cursor()
    sql = """
    UPDATE users
    SET password = %s
    WHERE user_id = %s
    """
    cur.execute(sql, (new_password, user_id))
    conn.commit()
    cur.close()
