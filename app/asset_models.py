from app import db
from app.models import Organisation

class DigitalAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)
    name = db.Column(db.String(1024), index=True, nullable=False)
    type = db.Column(db.String(1024), index=True, nullable=False)
    filename = db.Column(db.String(1024))