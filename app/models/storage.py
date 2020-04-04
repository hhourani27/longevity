from app import db
from app.models.asset import DigitalAsset, Collection

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    region = db.Column(db.String(120), nullable=False)
    
    ind_fragile_state_index = db.Column(db.String(10))
    ind_ict_dev_index = db.Column(db.String(10))
    ind_hdi = db.Column(db.String(10))
    
    assets = db.relationship('DataStorageLocation', backref='country', lazy='dynamic')
    
# Represent a Data Provider (Google, Amazon, Microsoft...)
class DataProvider(db.Model):
    __tablename__ = 'storage_data_provider'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    description = db.Column(db.String(1024))
    
    ind_current_ratio = db.Column(db.String(10))
    ind_quick_ratio = db.Column(db.String(10))
    ind_return_on_assets = db.Column(db.String(10))
    ind_accounts_receivable_turnover_ratio = db.Column(db.String(10))
    ind_operating_cash_flow_ratio = db.Column(db.String(10))
    ind_pretax_net_profit_margin = db.Column(db.String(10))
    ind_inventory_turnover = db.Column(db.String(10))
    
    data_storage_locations = db.relationship('DataStorageLocation', backref='data_provider', lazy='dynamic')

    
    def __repr__(self):
        return '<DataProvider {}>'.format(self.name)

# Represent a Data center location (Amazon Canada...)
class DataStorageLocation(db.Model):
    __tablename__ = 'storage_data_location'

    id = db.Column(db.Integer, primary_key=True)
    data_provider_id = db.Column(db.Integer, db.ForeignKey('storage_data_provider.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    longitude = db.Column(db.String(10))
    latitude = db.Column(db.String(10))

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

    def __repr__(self):
        return '<DigitalAssetStorage (digital_asset : {}, data_storage_location : {} )>'.format(self.asset_id,self.data_storage_location_id)


class AssetStorageHistory(db.Model):
    __tablename__ = 'storage_asset_history'
    
    EVENTS = {
        'STORED' : 'STORED',
        'READ_DATA' : 'READ_DATA'
        }

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('digital_asset.id'), nullable=False)
    event = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    data_storage_location_id = db.Column(db.Integer, db.ForeignKey('storage_data_location.id'))

    digital_asset = db.relationship('DigitalAsset', backref=db.backref('storage_history', lazy='dynamic'))
    storage_location = db.relationship('DataStorageLocation', backref=db.backref('storage_data_location', lazy='dynamic'))
    
class StorageStrategy(db.Model):
    __tablename__ = 'storage_strategy'
    
    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False, unique=True)
    strategy = db.Column(db.JSON, nullable=False)
    
    collection = db.relationship('Collection', backref='storage_strategy', uselist=False)