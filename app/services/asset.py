from app import app, db
from app.models.asset import DigitalAsset, DigitalAssetHistory
from app.services.storage import StorageService

class AssetService : 
    @staticmethod
    def add(digital_asset):
        db.session.add(digital_asset)
        
        event = DigitalAssetHistory(event=DigitalAssetHistory.EVENTS['CREATED'])
        event.digital_asset = digital_asset
        db.session.add(event)
        
        db.session.commit()

    @staticmethod    
    def add_and_store(digital_asset,data):
        print("ICI")
        print(type(data))
        AssetService.add(digital_asset)
        storage_locations = StorageService.storeAssetData(digital_asset,data)
        return storage_locations