from . import db
from sqlalchemy.sql import func

class recipeMaster(db.Model):
    __tablename__ = 'recipemaster'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50))
    #ingredients = db.relationship('Ingredients')

class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    #recipe_id = db.Column(db.Integer, db.ForeignKey('recipemaster.id'))
    ingredients = db.Column(db.String(50))
    amount = db.Column(db.Float)
    unit = db.Column(db.String(20))
    



