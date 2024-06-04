from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import csv
import psycopg2

#from flask import session
#from flask_session import Session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
db = ("dbname='musicapp' user='aurora' host='127.0.0.1' password='uis'")
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)


# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def import_data_from_csv(file_path, table_name, columns):
    # conn = psycopg2.connect("dbname='your_db' user='your_user' host='your_host' password='your_password'")
    cur = conn.cursor()

    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values = [row[column] for column in columns]
            sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
            cur.execute(sql, values)
    
    conn.commit()
    cur.close()
    conn.close()

# # Example usage:
# import_data_from_csv('artists.csv', 'artist', ['name'])
# import_data_from_csv('songs.csv', 'songs', ['name', 'artist_id', 'genre'])
# import_data_from_csv('profanity.csv', 'profanity', ['name'])
