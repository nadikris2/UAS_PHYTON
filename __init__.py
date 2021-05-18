from flask import Flask
from flask_login import LoginManager
from venv.instance.config import Config
from venv.models import db
from venv.auth import  views,forms
from venv.views import products, transactions,contactus
login_manager = LoginManager()

def create_app(config=Config):
	app = Flask(__name__)
	# load config
	app.config.from_object(config)
    
	# load sqlalchemy
	db.init_app(app)
        login_manager.init_app(app)
        login_manager.login_message = "You must be logged in to access this page."
        login_manager.login_view = "auth.login"


	# register blueprint
	app.register_blueprint(products.bp)
	app.register_blueprint(transactions.bp)
	app.register_blueprint(contactus.bp)

	return app