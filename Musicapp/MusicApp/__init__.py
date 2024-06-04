from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
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


