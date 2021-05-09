from . import db
#menarik data didalam database mysql untuk dapat di gunakan secara global 
class Contactus(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    users = db.Column(db.String(100), unique=True)
    hub = db.Column(db.String(100))
    isi = db.Column(db.String(100))