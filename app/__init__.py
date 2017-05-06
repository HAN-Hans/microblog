from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# creates the application object (of class Flask) 
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views, models