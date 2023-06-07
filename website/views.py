from http.client import BAD_REQUEST
import re
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from .models import recipeMaster, Ingredients, db, UserModel, Notes, Tags
from flask_login import current_user, login_required, login_user, logout_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    rows = recipeMaster.query.all()
    return render_template("index.html", rows=rows, id=id)

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = '%{0}%'.format(search_value)
        results = recipeMaster.query.filter(recipeMaster.recipe_name.like(search)).all()
        tagResults = Tags.query.filter(Tags.tag_name.like(search)).all()
        #query to set results equal to recipe_id and get that stuff
        i = 0
        getRecipeID = 0

        while i < len(tagResults):
            id = tagResults[i].recipe_id
            getRecipeID = recipeMaster.query.filter(recipeMaster.id == id).first()
            i+=1

        return render_template('search.html', results=results, tagResults = tagResults, getRecipeID = getRecipeID)
        

@views.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/add_recipe')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('views.addRecipe'))
     
    return render_template('login.html')

@views.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/add_recipe')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already associated with account')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@views.route('/recipe_base/<int:id>', methods=['GET', 'POST'])
def recipeBase(id=None):
    getID = request.path
    pages = re.search(r'(?<=/recipe_base/)\w+', getID)
    page = pages.group(0)
    names = recipeMaster.query.filter_by(id = page).first()
    ings = Ingredients.query.filter_by(recipe_id = page).all()
    customNotes = ""

    if current_user.is_authenticated:
        userID = current_user.id
        if request.method == 'POST':
            getNotes = request.form.get('customNote')
            data = Notes(recipe_id = page, creator_id = userID, note = getNotes)
            db.session.add(data)
            db.session.commit()
        customNotes = Notes.query.filter_by(recipe_id = page, creator_id = userID).all()

    return render_template('recipe_base.html', ings=ings, names=names, notes= customNotes)

@views.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def addRecipe():
    data = request.form
    createdBy = current_user.username

    if request.method == 'POST':        
        getRecipeName = request.form.get('recipeName')
        getSteps = request.form.get('Steps')
        data = recipeMaster(recipe_name = getRecipeName, steps = getSteps, created_by = createdBy)
        db.session.add(data)
        getTags = request.form.get('tags')
        getTags = getTags.split(',')
        print(len(getTags))
        i = 0
        getID = recipeMaster.query.filter_by(recipe_name = getRecipeName).first()
        getID = getID.id

        while i < len(getTags):
            db.session.add(Tags(recipe_id = getID, tag_name = getTags[i].replace(" ", "")))
            i+=1

        i = 0
        getI = request.form['getI']
        
        try:
            while i < int(getI):
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





    '''table for steps that has fk of recipe_id
button to add next step and remove

Logo on mobile

have log in/register disappear if logged in

delete personal notes'''

