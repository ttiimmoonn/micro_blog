from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# основной объект приложения
app = Flask(__name__)
app.config.from_object(Config)

# объкт базы данных
db = SQLAlchemy(app)

# объект миграции базы данных
migrate = Migrate(app, db)

from app import routes, models
