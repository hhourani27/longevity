from app import db
from app.models.asset import DigitalAsset

class Format(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50))
    extension = db.Column(db.String(50), nullable=False)
    
    assets = db.relationship('DigitalAsset', backref='format', lazy='dynamic')

    def __repr__(self):
        return '<Format : {}>'.format(self.name)
    
    def display_name(self):
        return '{}/{}'.format(self.media,self.name)
        