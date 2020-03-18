from app import app, db
from app.models.asset import DigitalAsset

class AssetManager : 
    @staticmethod
    def add(digital_asset):
        db.session.add(digital_asset)
        db.session.commit()
