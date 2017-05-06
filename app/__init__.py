from flask import Flask

# creates the application object (of class Flask) 
app = Flask(__name__)
app.config.from_object('config')

from app import views