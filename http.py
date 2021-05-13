from flask import Flask
from venv.config import Config
from venv.models import db
from venv.views import products, transactions,contactus

def create_app(config=Config):
	app = Flask(__name__)
	# load config
	app.config.from_object(config)

	# load sqlalchemy
	db.init_app(app)

	# register blueprint
	app.register_blueprint(products.bp)
	app.register_blueprint(transactions.bp)
	app.register_blueprint(contactus.bp)
	return app