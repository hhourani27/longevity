from pathlib import Path
import random
from sqlalchemy import func
from abc import ABC, abstractmethod
from app import app, db
from app.models.storage import DataProvider, DataStorageLocation, DigitalAssetStorage, AssetStorageHistory

class StorageSelector : 
    @staticmethod
    def getStorageLocation_random(count = 1):
        data_providers = DataProvider.query.all()
        
        selected_data_providers = dict()
        for dp in data_providers:
            selected_data_providers[dp] = 0
        
        for i in range(count):
            dp = random.choice(data_providers)
            selected_data_providers[dp] = selected_data_providers[dp] + 1
        
        selected_storage_locations = []
        for dp,n in selected_data_providers.items():
            if n > 0 :
                selected_storage_locations.extend(DataStorageLocation.query.filter_by(data_provider=dp).order_by(func.random()).limit(n).all())
            
        return selected_storage_locations

class StorageService():
    def storeAssetData(digital_asset,data):
        storage_locations = StorageSelector.getStorageLocation_random(count=5)
        
        storageManagers = []
        for sl in storage_locations:
            if sl.data_provider.name == 'Google':
                storageManagers.append(LocalFileStorageManager(sl))
            elif sl.data_provider.name == 'Amazon':
                storageManagers.append(LocalFileStorageManager(sl))
            elif sl.data_provider.name == 'Microsoft':
                storageManagers.append(LocalFileStorageManager(sl))
        
        for sm in storageManagers:
            sm.storeAssetData(digital_asset,data)
            
        return storage_locations

class StorageManager(ABC) :

    def storeAssetData(self,digital_asset,data) :
        self.storeAssetData_internal(digital_asset,data)
        
        event = AssetStorageHistory(event=AssetStorageHistory.EVENTS['STORED'])
        event.digital_asset = digital_asset
        event.storage_location = self.data_storage_location
        db.session.add(event)
        db.session.commit()

    @abstractmethod
    def storeAssetData_internal(self,digital_asset,data) :
        pass

class LocalFileStorageManager(StorageManager) :
    def __init__(self,data_storage_location):
        self.data_storage_location=data_storage_location
    
    def storeAssetData_internal(self,digital_asset,data):
        
        # Save data in file storage
        data_provider_path = Path(app.config['STORAGE_FILE_LOCATION']).joinpath(str(self.data_storage_location.data_provider.id))
        if not data_provider_path.exists() :
            data_provider_path.mkdir()
        
        data_storage_path = data_provider_path.joinpath(str(self.data_storage_location.id))
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
        asset_storage.data_storage_location = self.data_storage_location
        asset_storage.digital_asset = digital_asset
        
        db.session.add(asset_storage)
        db.session.commit()