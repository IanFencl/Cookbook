from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path



db = SQLAlchemy()
DB_NAME = "cookbook.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'VERYSECRETKEY'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import recipeMaster, Ingredients, login

    create_database(app)

    login.init_app(app)
    login.login_view = 'views.login'

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        #db.drop_all()
        db.create_all(app=app)
        db.session.commit()
        print('Created Database!')

