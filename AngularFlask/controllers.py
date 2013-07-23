import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from AngularFlask import app

###
# controllers/routing for API endpoints
# (auto-generated from the models listed in app.config['API_MODELS'])
###
from AngularFlask.core import api_manager
from AngularFlask.models import *

api_models = app.config['API_MODELS']
for model_name in api_models:
	model_class = api_models[model_name]
	api_manager.create_api(model_class, methods=['GET', 'POST'])

session = api_manager.session

###
# controllers/routing for basic pages (pass routing onto the Angular app)
###
@app.route('/')
@app.route('/about')
@app.route('/blog')
def basic_pages(**kwargs):
	return make_response(open('AngularFlask/templates/index.html').read())

###
# controllers/routing for CRUD-style endpoints, or ones that refer to a particular resource or collection
# (pass routing onto the Angular app only if the corresponding resource exists in the db)
###
from sqlalchemy.sql import exists

crud_url_models = app.config['CRUD_URL_MODELS']

@app.route('/<model_name>/')
@app.route('/<model_name>/<item_id>')
def rest_pages(model_name, item_id=None):
	if model_name in crud_url_models:
		model_class = crud_url_models[model_name]
		if item_id is None or session.query(exists().where(model_class.id == item_id)).scalar():
			return make_response(open('AngularFlask/templates/index.html').read())
	abort(404)

###
# special file handlers
##
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

###
# error handlers
##
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



