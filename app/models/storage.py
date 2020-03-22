from app import db
from app.models.asset import DigitalAsset

# Represent a Data Provider (Google, Amazon, Microsoft...)
class DataProvider(db.Model):
    __tablename__ = 'storage_data_provider'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    
    data_storage_locations = db.relationship('DataStorageLocation', backref='data_provider', lazy='dynamic')

    
    def __repr__(self):
        return '<DataProvider {}>'.format(self.name)

# Represent a Data center location (Amazon Canada...)
class DataStorageLocation(db.Model):
    __tablename__ = 'storage_data_location'

    id = db.Column(db.Integer, primary_key=True)
    data_provider_id = db.Column(db.Integer, db.ForeignKey('storage_data_provider.id'), nullable=False)
    name = db.Column(db.String(120), index=True, nullable=False)
    continent = db.Column(db.String(120), index=True, nullable=False)
    country = db.Column(db.String(120), index=True, nullable=False)

    def __repr__(self):
        return '<DataStorageLocation (data_provider : {}, name : {} )>'.format(self.data_provider.name,self.name)

# Association table
class DigitalAssetStorage(db.Model):
    __tablename__ = 'storage_asset'

    asset_id = db.Column(db.Integer, db.ForeignKey('digital_asset.id'), primary_key=True)
    data_storage_location_id = db.Column(db.Integer, db.ForeignKey('storage_data_location.id'), primary_key=True)
    uri = db.Column(db.String(1024))
    
    data_storage_location = db.relationship('DataStorageLocation', backref='digital_assets')
    digital_asset = db.relationship('DigitalAsset', backref='storage_locations')

class AssetStorageHistory(db.Model):
    __tablename__ = 'storage_asset_history'
    
    EVENTS = {
        'STORED' : 'STORED'
        }

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('digital_asset.id'), nullable=False)
    event = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    data_storage_location_id = db.Column(db.Integer, db.ForeignKey('storage_data_location.id'))

    digital_asset = db.relationship('DigitalAsset', backref=db.backref('storage_history', lazy='dynamic'))
    storage_location = db.relationship('DataStorageLocation', backref=db.backref('storage_data_location', lazy='dynamic'))