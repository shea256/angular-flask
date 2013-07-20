import os
import argparse

from AngularFlask.core import db
from AngularFlask.models import Post

def create_sample_db_entry(api_endpoint, datasource_path):
	os.system('curl localhost:5000/' + api_endpoint + ' -X POST -d @' + datasource_path + ' -H "Content-Type: application/json"')
	
def create_db():
	db.create_all()

def drop_db():
	db.drop_all()

def main():
	parser = argparse.ArgumentParser(description='Manage this Flask application.')
	parser.add_argument('command', help='the name of the command you want to run')
	parser.add_argument('--seed_db', help='whether you want to seed the database with sample data', action='store_const', const=True)
	args = parser.parse_args()

	if args.command == 'create_db':
		create_db()
		print "DB created!"
		if args.seed_db:
			create_sample_db_entry('api/post', 'data/post1.json')
			print "\nSample blogpost entry added to database!"
	elif args.command == 'delete_db':
		drop_db()
		print "DB deleted!"
	else:
		raise Exception('Invalid command')

if __name__ == '__main__':
	main()
