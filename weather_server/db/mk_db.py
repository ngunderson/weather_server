from model import db
from weather_server.server import create_app
create_app().app_context().push()

#print 'Uncomment this file to create a new db based on model.py'
db.create_all()
