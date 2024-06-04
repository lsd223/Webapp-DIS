# write all your SQL queries in this file.

from MusicApp import conn, login_manager
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
    SELECT * FROM artist WHERE name ILIKE %s
    """
    cur.execute(sql, (name))
    artists = cur.fetchall()
    cur.close()
    return artists

def select_song(title):
    cur = conn.cursor()
    sql = """
    SELECT * FROM song WHERE title ILIKE %s
    """
    cur.execute(sql, (title))
    songs = cur.fetchall()
    cur.close()
    return songs

def select_profanity(word):
    cur = conn.cursor()
    sql = """
    SELECT * FROM profanity WHERE word ILIKE %s
    """
    cur.execute(sql, (word))
    profanity_words = cur.fetchall()
    cur.close()
    return profanity_words


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
