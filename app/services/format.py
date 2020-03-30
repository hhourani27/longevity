from app import app, db
from app.models.format import Format
    
  
class FormatService :
    @staticmethod
    def get_all():
        formats = Format.query.all()
        return formats