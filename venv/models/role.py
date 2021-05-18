# pos/models/products.py
from venv.models import db

#menarik data didalam database mysql untuk dapat di gunakan secara global 

class role(Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    users = db.relationship('Users', backref='role', lazy=True)
    
    
    def __repr__(self):
        return '<role %r>' % self.name

    def create(self, name):
        role=role(name=name)
           
        db.session.add(role)
        db.session.commit()

    def update(self,name,role_id):
         role = role.query.filter_by(id=role_id).first()
         role.name=name
         db.session.commit()


    def delete(self,id):
        role = role.query.filter_by(id=role_id).first()
        db.session.delete(role)
        db.session.commit()