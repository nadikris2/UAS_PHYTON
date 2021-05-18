from venv.models import db
from sqlalchemy.orm import relationship
from sqlalchemy import event
from venv.models.products import Products
#menarik data didalam database mysql untuk dapat di gunakan secara global 
class role(db.Model):
	roleID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	roleName = db.Column(db.Integer, nullable=False)



