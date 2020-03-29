from pathlib import Path
import random
from sqlalchemy import func
from abc import ABC, abstractmethod
from app import app, db
from app.models.asset import DigitalAsset
from app.models.storage import DataProvider, DataStorageLocation, DigitalAssetStorage, AssetStorageHistory
from flask_login import current_user

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
    @staticmethod
    def storeAssetData(digital_asset,data):
    
        # Select random storage locations
        storage_locations = StorageSelector.getStorageLocation_random(count=3)
        
        # Create Storage Manager objects
        storageManagers = []
        for sl in storage_locations:
            storageManagers.append(StorageManager.getStorageManager(sl))
        
        # For each Storage Manager object, store the data
        for sm in storageManagers:
            sm.storeAssetData(digital_asset,data)
        
        # Return the storage locations
        return storage_locations

    @staticmethod
    def getAssetData(digital_asset):
        # Get the first storage location where the asset is stored
        asset_storage = DigitalAssetStorage.query.filter_by(asset_id=digital_asset.id).first()
        storage_location = asset_storage.data_storage_location
        
        # Create the Storage Manager object
        storageManager = StorageManager.getStorageManager(storage_location)
        
        # Get the data
        data = storageManager.getAssetData(digital_asset)
        
        # Create read event
        event = AssetStorageHistory(event=AssetStorageHistory.EVENTS['READ_DATA'])
        event.digital_asset = digital_asset
        event.storage_location = storage_location
        db.session.add(event)
        db.session.commit()
        
        return data

    @staticmethod        
    def getStorageLocations(collection = None, used_only=False):
        query = db.session().query(DataStorageLocation).join(DigitalAssetStorage).join(DigitalAsset).filter(DigitalAsset.organisation_id==current_user.organisation_id)
        
        if collection is not None : 
           query = query.filter(DigitalAsset.collection_id == collection.id)     
        
        storage_locations = query.all()
        
        return storage_locations

    @staticmethod        
    def getStorageRegions(collection = None, used_only=False):
        storage_locations = StorageService.getStorageLocations(collection=collection, used_only=used_only)
        storage_regions = list(set([sl.continent for sl in storage_locations]))
        storage_regions.sort()
        
        return storage_regions
        
    @staticmethod        
    def getDataProviders(collection = None, used_only=False):
        storage_locations = StorageService.getStorageLocations(collection=collection, used_only=used_only)
        storage_providers = list(set([sl.data_provider for sl in storage_locations]))
        storage_providers.sort(key = lambda p: p.name)
        
        return storage_providers

    @staticmethod        
    def getDataReadCount(collection = None):
        query = (
            db.session.query(AssetStorageHistory)
            .join(DigitalAsset).
            filter(DigitalAsset.organisation_id==current_user.organisation_id, AssetStorageHistory.event==AssetStorageHistory.EVENTS['READ_DATA'])
            )
        
        if collection is not None : 
            query = query.filter(DigitalAsset.collection_id == collection.id)
        
        read_count = query.count()
        
        return read_count
        

# A class that manages communication with a Data Location
class StorageManager(ABC) :

    @staticmethod
    def getStorageManager(storage_location) :
        if storage_location.data_provider.name == 'Google':
            return LocalFileStorageManager(storage_location)
        elif storage_location.data_provider.name == 'Amazon':
            return LocalFileStorageManager(storage_location)
        elif storage_location.data_provider.name == 'Microsoft':
            return LocalFileStorageManager(storage_location)    

    @abstractmethod
    def getAssetData(self, digital_asset) :
        pass   

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

    def getAssetData(self,digital_asset) :
        asset_storage = DigitalAssetStorage.query.filter_by(asset_id=digital_asset.id, data_storage_location_id=self.data_storage_location.id).first()
        file_path = Path(asset_storage.uri[10:]) # Remove file:// part of the uri
        data = file_path.read_bytes()
        return data
    
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
        file_path.write_bytes(data)
        
        # Add digital_asset_storage entry in db
        asset_storage = DigitalAssetStorage(uri=file_path.as_uri())
        asset_storage.data_storage_location = self.data_storage_location
        asset_storage.digital_asset = digital_asset
        
        db.session.add(asset_storage)
        db.session.commit()