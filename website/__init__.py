
# Import Modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Setup Database
db = SQLAlchemy()
DB_NAME = "portfolio.db"

# Setup App
def create_app():
    
    # Initalize DB
    app = Flask(__name__)
    
    # Setup Key and Database
    app.config['SECRET_KEY'] = 'password'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    
    # Import Routes
    from .views import views

    # Setup Views & Authentification
    app.register_blueprint(views, url_prefix='/')

    
    # Establish DB
    with app.app_context():
        db.create_all()

    return app

# Create Database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')