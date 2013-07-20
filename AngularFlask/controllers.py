import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from AngularFlask import app

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# basic page url handler
@app.route('/')
@app.route('/about')
def basic_pages(**kwargs):
	return make_response(open('AngularFlask/templates/index.html').read())

# API
from AngularFlask.core import api_manager
from AngularFlask.models import Post

session = api_manager.session

api_manager.create_api(Post, methods=['GET', 'POST'])

# RESTful page url handler
from sqlalchemy.sql import exists

supported_models = ['post']

@app.route('/<model_name>')
@app.route('/<model_name>/<item_id>')
def rest_pages(model_name, item_id=None):
	if model_name in supported_models:
		model = eval(model_name.capitalize())
		if session.query(exists().where(model.id == item_id)).scalar():
			return make_response(open('AngularFlask/templates/index.html').read())
	abort(404)


