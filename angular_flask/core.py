from angular_flask import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)
