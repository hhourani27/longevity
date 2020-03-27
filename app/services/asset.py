from app import app, db
from app.models.asset import DigitalAsset, DigitalAssetHistory, Collection
from app.services.storage import StorageService
from flask_login import current_user

class AssetService : 
    @staticmethod
    def count(collection=None):
        if collection is None :
            return DigitalAsset.query.filter_by(organisation_id=current_user.organisation.id).count()
        else :
            return DigitalAsset.query.filter_by(organisation_id=current_user.organisation.id, collection_id=collection.id).count()
            
    @staticmethod
    def get(id) :
        asset = DigitalAsset.query.filter_by(id=id, organisation_id=current_user.organisation_id).first()
        
        if asset is not None :
            event = DigitalAssetHistory(event=DigitalAssetHistory.EVENTS['READ'])
            event.digital_asset = asset
            db.session.add(event)
            db.session.commit()
        
        return asset

    @staticmethod
    def add(digital_asset):
        db.session.add(digital_asset)
        
        event = DigitalAssetHistory(event=DigitalAssetHistory.EVENTS['CREATED'])
        event.digital_asset = digital_asset
        db.session.add(event)
        
        db.session.commit()

    @staticmethod
    def add_and_store(digital_asset,data):
        AssetService.add(digital_asset)
        storage_locations = StorageService.storeAssetData(digital_asset,data)
        return storage_locations
        

        
class CollectionService :
    @staticmethod
    def get_all():
        collections = Collection.query.filter_by(organisation_id=current_user.organisation.id).all()
        return collections if collections is not None else []
    
    @staticmethod
    def count():
        return Collection.query.filter_by(organisation_id=current_user.organisation.id).count() 
