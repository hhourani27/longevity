from app import db
from app.models import Organisation
from app.storage_models import DataStorageLocation

    
digital_asset_storage = db.Table('digital_asset_storage',
    db.Column('asset_id', db.Integer, db.ForeignKey('digital_asset.id'), primary_key=True),
    db.Column('data_storage_location_id', db.Integer, db.ForeignKey('data_storage_location.id'), primary_key=True),
    db.Column('uri', db.String(1024), nullable=False)
    )


class DigitalAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)
    name = db.Column(db.String(1024), index=True, nullable=False)
    type = db.Column(db.String(1024), index=True, nullable=False)
    
    storage_locations = db.relationship('DataStorageLocation', secondary=digital_asset_storage, primaryjoin = (digital_asset_storage.c.asset_id == id),secondaryjoin = (digital_asset_storage.c.data_storage_location_id == id), backref = db.backref('assets', lazy='dynamic'), lazy='dynamic')
        