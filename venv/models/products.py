# pos/models/products.py
from venv.models import db
#menarik data didalam database mysql untuk dapat di gunakan secara global 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)