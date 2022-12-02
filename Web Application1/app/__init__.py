#import function which is required to initialize
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#initializes the migration
migrate = Migrate(app,db)

from app import views, models
