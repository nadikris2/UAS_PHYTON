from flask import Flask
from flask_login import LoginManager
from venv.instance.config import Config
from venv.models import db
from venv.login.auth import  views,forms
from venv.views import products, transactions,contactus
from flask_bootstrap import Bootstrap
from venv.login.config import app_config
from venv.login import models,home,admin,auth

from flask_sqlalchemy import SQLAlchemy
login_manager = LoginManager()

db = SQLAlchemy()


def create_app(config=Config):
	app = Flask(__name__)
	Bootstrap(app)
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
	app.register_blueprint(admin.blueprint,url_prifx='/admin')
	app.register_blueprint(auth.blueprint)
	app.register_blueprint(home.blueprint)



	return app