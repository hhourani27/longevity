from app import app, db
from app.models.asset import DigitalAsset
from app.services.storage import StorageService

class AssetManager : 
    @staticmethod
    def add(digital_asset):
        db.session.add(digital_asset)
        db.session.commit()

    @staticmethod    
    def add_and_store(digital_asset,data):
        db.session.add(digital_asset)
        storage_locations = StorageService.storeAssetData(digital_asset,data)
        return storage_locations