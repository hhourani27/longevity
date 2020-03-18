from app import db, login
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        print(self.password_hash)
        print(password)
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    users = db.relationship('User', backref='organisation', lazy='dynamic')
    
    def __repr__(self):
        return '<Organisation {}>'.format(self.name)
