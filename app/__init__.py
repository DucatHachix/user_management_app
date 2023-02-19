import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(    
    os.environ.get('DB_USER', 'app_user'),
    os.environ.get('DB_PASS', 'app_password'),
    os.environ.get('DB_HOST', 'app'),
    os.environ.get('DB_NAME', 'app_db')
)
db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from app import routes, models