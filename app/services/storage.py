from pathlib import Path
from sqlalchemy import func
from app import app, db
from app.models.storage import DataProvider, DataStorageLocation, DigitalAssetStorage

class StorageSelector : 
    @staticmethod
    def getStorageLocation():
        data_provider = DataProvider.query.order_by(func.random()).first()
        data_storage_location = DataStorageLocation.query.filter_by(data_provider=data_provider).order_by(func.random()).first()
        return data_storage_location
        
class StorageManager :
    @staticmethod
    def storeAsset(digital_asset,data):
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