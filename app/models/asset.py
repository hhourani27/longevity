from app import db
from app.models.user import Organisation

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)
    name = db.Column(db.String(1024), index=True, nullable=False)
    description = db.Column(db.String(1024), index=True, nullable=False)
    
    assets = db.relationship('DigitalAsset', backref='collection', lazy='dynamic')

    def __repr__(self):
        return '<Collection {}>'.format(self.name)

class DigitalAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)
    name = db.Column(db.String(1024), index=True, nullable=False)
    type = db.Column(db.String(1024), index=True, nullable=False)
    filename = db.Column(db.String(1024))
        
class DigitalAssetHistory(db.Model):
    EVENTS = {
        'CREATED' : 'CREATED'
        }

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('digital_asset.id'), nullable=False)
    event = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    details = db.Column(db.String(1024))
    
    digital_asset = db.relationship('DigitalAsset', backref=db.backref('asset_history', lazy='dynamic'))
