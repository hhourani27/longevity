from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

#app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

from app import routes, models, asset_models, storage_models
