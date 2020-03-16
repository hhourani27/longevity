from pathlib import Path
from app import app,db
from app.asset_models import DigitalAsset
from sqlalchemy import func

class DataProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    
    data_storage_locations = db.relationship('DataStorageLocation', backref='data_provider', lazy='dynamic')

    
    def __repr__(self):
        return '<DataProvider {}>'.format(self.name)

class DataStorageLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_provider_id = db.Column(db.Integer, db.ForeignKey('data_provider.id'), nullable=False)
    name = db.Column(db.String(120), index=True, nullable=False)
    continent = db.Column(db.String(120), index=True, nullable=False)
    country = db.Column(db.String(120), index=True, nullable=False)

    def __repr__(self):
        return '<DataStorageLocation (data_provider : {}, name : {} )>'.format(self.data_provider.name,self.name)

#Association table
class DigitalAssetStorage(db.Model):
    asset_id = db.Column(db.Integer, db.ForeignKey('digital_asset.id'), primary_key=True)
    data_storage_location_id = db.Column(db.Integer, db.ForeignKey('data_storage_location.id'), primary_key=True)
    uri = db.Column(db.String(1024))
    
    data_storage_location = db.relationship('DataStorageLocation', backref='digital_assets')
    digital_asset = db.relationship('DigitalAsset', backref='storage_locations')


class StorageSelector : 
    @staticmethod
    def getStorageLocation():
        data_provider = DataProvider.query.order_by(func.random()).first()
        data_storage_location = DataStorageLocation.query.filter_by(data_provider=data_provider).order_by(func.random()).first()
        return data_storage_location
        
class StorageManager :
    @staticmethod
    def saveAsset(digital_asset,data):
        # Pick storage location
        data_storage_location = StorageSelector.getStorageLocation()
        
        # Save data in file storage
        data_provider_path = Path(app.config['STORAGE_FILE_LOCATION']).joinpath(str(data_storage_location.data_provider.id))
        if not data_provider_path.exists() :
            data_provider_path.mkdir()
        
        data_storage_path = data_provider_path.joinpath(str(data_storage_location.id))
        if not data_storage_path.exists():
            data_storage_path.mkdir()
        
        filename = digital_asset.filename
        file_storage_name = str(digital_asset.id)
        if '.' in filename:
            file_storage_name += filename[filename.find('.'):]
        
        file_path = data_storage_path.joinpath(file_storage_name)
        data.save(file_path)
        
        # Add digital_asset_storage entry in db
        asset_storage = DigitalAssetStorage(uri=file_path.as_uri())
        asset_storage.data_storage_location = data_storage_location
        asset_storage.digital_asset = digital_asset
        
        db.session.add(asset_storage)
        db.session.commit()