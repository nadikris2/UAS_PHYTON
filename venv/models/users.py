# pos/models/products.py
from venv.models import db
from flask_login import UserMixin
#menarik data didalam database mysql untuk dapat di gunakan secara global 

class users(UserMixin.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45),nullable=False)
    password = db.Column(db.String(45),nullable=False)
    roleID= db.Column(db.Integer, db.ForeignKey("role.id"),nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

    def create(self, name, email, password, role_id):
        users=users(
            name=name,
            email=email,
            password=password,
            role_id=role_id
        )

        db.session.add(users)
        db.session.commit()

    def update(self,name,email,password,id):
         users = users.query.filter_by(id=id).first()
         users.name=name,
         users.email=email,
         users.password=password,
         users.id=id
         db.session.commit()
         
    def update_password(self,password,id):
        users=users.query.filter_by(id=id).first()
        users.password = password
        db.session.commit()

    def delete(self,id):
        users = users.query.filter_by(id=id).first()
        db.session.delete(users)
        db.session.commit()

@login_manager.user_loader
def load_user(id):
    return users.query.get(int(id))