import os
from flask import Flask, render_template, url_for, request, session, redirect, flash, send_from_directory
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import random
import bcrypt


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'Bakery_Wikipedia'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
    
@app.route('/recipes')
def recipes():
    return render_template('recipes.html',
    categories=mongo.db.categories.find(),
    subcategory=mongo.db.subcategory.find(),
    recipes=mongo.db.recipes.find())
    
    
@app.route('/recipespage/<recipe_id>', methods=['GET', 'POST'])
def recipespage(recipe_id):
    """Route to show single recipe view page"""
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) #Here you are only finding one!
    all_recipes = mongo.db.recipes.find().limit(4)#Pass them all down to the view and iterate over this and not just 1! hahahahaha
    return render_template('recipes_name.html', recipes=recipes, all_recipes=all_recipes)
    
	
	
@app.route('/suggested_recipespage/<recipe_id>', methods=['GET', 'POST'])
def suggested_recipespage(recipes_id):
    """Route to take the user to the suggested recipe chosen"""
    recipes = mongo.db.recipes.find({"_id": ObjectId(recipes_id)})
    return render_template('recipes_name.html', recipes=recipes)
    
    
@app.route('/login')
def login():
    return render_template('Login.html')
    
    
@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    """Function for handling the logging in of users"""
    user = mongo.db.users
    logged_in_user = user.find_one({
            'name': request.form['name']})
    print(logged_in_user)
                                
    if logged_in_user: # If the username is in the db then check the password
        if logged_in_user['password'] == request.form['pass']: # If password matches
            session['name'] = request.form['name'] #Set the session username
            session['logged_in'] = True #Set the logged_in flag
            print('Going to the users route')
            return redirect(url_for('users'))
        print('Sorry wrong pass')
        flash('Sorry incorrect password!') #If password is incorrect
        return redirect(url_for('login'))
    flash('sorry something went wrong')
    return redirect(url_for('login'))
    
    
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # Kill session
    return redirect(url_for('index'))

    
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/users')
def users():
    return render_template('userpage.html', users=mongo.db.users.find(),
    recipes=mongo.db.recipes.find())
    

@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        user = mongo.db.users  #Load your user collection
        existing_user = user.find_one({'name': request.form['name']}) #Check if user already exists
        
        
        if existing_user is None:  #If user doesn't exist then lets register them
            user.insert(request.form.to_dict()) #I'd map the fields manually and not use to_dict() method..
            session['name'] = request.form['name'] #Upon successful registration set the username to the session
            print(session['name'])
            session['logged_in'] = True # Set a indicator to help user later on
            flash('You are now registered')
            return redirect(url_for('users'))
        flash('Sorry username already exists!')
        return redirect(url_for('register'))
	
    return render_template('userpage.html')

    
@app.route('/recipe_name')
def recipe_name():
    return render_template('userpage.html', rec=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find(),
    subcategory=mongo.db.subcategory.find())
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    if request.method == 'POST':
        tasks = mongo.db.recipes
        existing_recipe = tasks.find_one({'name' : request.form['name']})
    
    if existing_recipe is None:
        tasks.insert_one({
            'category_name': request.form['category_name'],
            'subcategory_name': request.form['subcategory_name'],
            'name': request.form['name'],
            'ingredient': request.form.get('ingredient', ""),
            'ingredient1': request.form.get('ingredient1', ""),
            'ingredient2': request.form.get('ingredient2', ""),
            'ingredient3': request.form.get('ingredient3', ""),
            'ingredient4': request.form.get('ingredient4', ""),
            'ingredient5': request.form.get('ingredient5', ""),
            'ingredient6': request.form.get('ingredient6', ""),
            'ingredient7': request.form.get('ingredient7', ""),
            'ingredient8': request.form.get('ingredient8', ""),
            'ingredient9': request.form.get('ingredient9', ""),
            'ingredient10': request.form.get('ingredient10', ""),
            'ingredient11': request.form.get('ingredient11', ""),
            'ingredient12': request.form.get('ingredient12', ""),
            'ingredient13': request.form.get('ingredient13', ""),
            'ingredient14': request.form.get('ingredient14', ""),
            'ingredient15': request.form.get('ingredient15', ""),
            'ingredient16': request.form.get('ingredient16', ""),
            'ingredient17': request.form.get('ingredient17', ""),
            'ingredient18': request.form.get('ingredient18', ""),
            'ingredient19': request.form.get('ingredient19', ""),
            'ingredient20': request.form.get('ingredient20', ""),
            'ingredient21': request.form.get('ingredient21', ""),
            'ingredient22': request.form.get('ingredient22', ""),
            'ingredient23': request.form.get('ingredient23', ""),
            'ingredient24': request.form.get('ingredient24', ""),
            'instruction': request.form.get('instruction', ""),
            'instruction1': request.form.get('instruction1', ""),
            'instruction2': request.form.get('instruction2', ""),
            'instruction3': request.form.get('instruction3', ""),
            'instruction4': request.form.get('instruction4', ""),
            'instruction5': request.form.get('instruction5', ""),
            'instruction6': request.form.get('instruction6', ""),
            'instruction7': request.form.get('instruction7', ""),
            'instruction8': request.form.get('instruction8', ""),
            'instruction9': request.form.get('instruction9', ""),
            'instruction10': request.form.get('instruction10', ""),
            'instruction11': request.form.get('instruction11', ""),
            'instruction12': request.form.get('instruction12', ""),
            'instruction13': request.form.get('instruction13', ""),
            'instruction14': request.form.get('instruction14', ""),
            'description': request.form['description'],
            'kcal' : request.form['kcal'],
            'fat': request.form['fat'],
            'saturates': request.form['saturates'],
            'carbs': request.form['carbs'],
            'sugars': request.form['sugars'],
            'fibre': request.form['fibre'],
            'protein': request.form['protein'],
            'salt': request.form['salt'],
            'image_url': request.form['image_url'],
            'author': session['name'].title(), #See author now can be added
    		'approval': 'no', # And approval 
        })
        return redirect(url_for('recipes'))
    flash('Sorry recipe already exists!')
    return redirect(url_for('add_recipe'))
    
    
@app.route('/admin')
def admin():
    return render_template('admin.html', users=mongo.db.users.find(), 
    recipes=mongo.db.recipes.find())
    
    
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('admin'))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('admin'))
    
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update_many({"_id": ObjectId(recipe_id)}, {"$set": {"approval": "yes"}})
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.secret_key = 'Hello'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)