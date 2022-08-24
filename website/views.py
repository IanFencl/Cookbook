from http.client import BAD_REQUEST
import re
from flask import Blueprint, render_template, request, redirect, url_for
from .models import recipeMaster, Ingredients, db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    rows = recipeMaster.query.all()
    return render_template("index.html", rows=rows)

@views.route('/recipe_base', methods=['GET', 'POST'])
def recipeBase():
    return render_template('recipe_base.html')

@views.route('/add_recipe', methods=['GET', 'POST'])
def addRecipe():
    data = request.form
    #data = data.to_dict(flat=False)
    #print(data)

    if request.method == 'POST':        
        getRecipeName = request.form.get('recipeName')
        getSteps = request.form.get('Steps')
        data = recipeMaster(recipe_name = getRecipeName, steps = getSteps)
        db.session.add(data)
        #db.session.commit()
    
    #getIngredient = 'start'
        i = 0
    #if (request.method == 'POST'):
        getI = request.form['getI']
        #print(getI)
        getID = recipeMaster.query.filter_by(recipe_name = getRecipeName).first()
        getID = getID.id
        try:
            while i < int(getI): #getIngredient != '' and request.method == 'POST':
                getIngredient = request.form['Ingredient' + str(i)]
                getAmount = request.form['Amount' + str(i)]
                getUnit = request.form['Unit' + str(i)]
                data = Ingredients(recipe_id = str(getID), ingredients = getIngredient, amount = getAmount, unit = getUnit)
                db.session.add(data)
                db.session.commit()
                print(getIngredient, getAmount, getUnit)
                i+=1
        except KeyError:
            print("key error")
        
        finally:
            print("done")
    return render_template("add_recipe.html")