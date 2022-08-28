from . import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
 
login = LoginManager()

class recipeMaster(db.Model):
    __tablename__ = 'recipemaster'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50))
    steps = db.Column(db.String(2000))
    created_by = db.Column(db.String(50))
    #ingredients = db.relationship('Ingredients')

class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipemaster.id'))
    ingredients = db.Column(db.String(50))
    amount = db.Column(db.String)
    unit = db.Column(db.String(20))
    
class Notes(db.Model):
    note_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer)
    note = db.Column(db.String(1000))

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())
 
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
     
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

