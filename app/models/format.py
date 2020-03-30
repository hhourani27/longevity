from app import db
from app.models.asset import DigitalAsset

class Format(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), index=True, nullable=False)
    subtype = db.Column(db.String(50), index=True, nullable=False)
    
    assets = db.relationship('DigitalAsset', backref='format', lazy='dynamic')

    def display_name(self):
        return "{}/{}".format(self.type,self.subtype)

    def __repr__(self):
        return '<Format : {}/{}>'.format(self.type,self.subtype)