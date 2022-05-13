from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# setting up database
# database initialization
# db is the object that can be used to add & create to/from the database
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)  # initialize the app

    # encrypt/secure the cookies and session data of website
    app.config['SECRET_KEY'] = 'secret key'  # random string
    # creating the database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initializing the database by giving the flask app
    db.init_app(app)

    # importing the blueprints
    from .views import views
    from .auth import auth

    # registering the imported blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    # were to go if not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app  # return the app

# to check if the database already exists, if not it will create it


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
