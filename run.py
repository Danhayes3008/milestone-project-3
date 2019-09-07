# this is the backbone of my site. In it are all the routes that control the content in my site aswell as directs the user from page to page.

import os
from flask import Flask, render_template, url_for, request, session, redirect, flash, send_from_directory
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import random
import bcrypt


app = Flask(__name__)

# This part controls were the data is being called from
app.config["MONGO_DBNAME"] = 'Bakery_Wikipedia'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

# This is the route that diplays the homepage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
# This is the route that diplays the recipes page and checks the database for the collections below    
@app.route('/recipes')
def recipes():
    categories = mongo.db.categories.find()
    return render_template('recipes.html', categories=categories)

# Below are the routes that display the category pages
@app.route('/breads')
def breads():
    recipes=mongo.db.recipes.find()
    return render_template('bread.html', recipes=recipes)
    
@app.route('/GlutenFree')
def GlutenFree():
    recipes=mongo.db.recipes.find()
    return render_template('Gluten-Free.html', recipes=recipes)
    
@app.route('/cakes')
def cakes():
    recipes=mongo.db.recipes.find()
    return render_template('cakes.html', recipes=recipes)
    
@app.route('/Tarts')
def Tarts():
    recipes=mongo.db.recipes.find()
    return render_template('Tarts.html', recipes=recipes)
    
@app.route('/Pies')
def Pies():
    recipes=mongo.db.recipes.find()
    return render_template('Pies.html', recipes=recipes)
    
@app.route('/Biscuits')
def Biscuits():
    recipes=mongo.db.recipes.find()
    return render_template('Biscuits.html', recipes=recipes)
    
@app.route('/Deserts')
def Deserts():
    recipes=mongo.db.recipes.find()
    return render_template('Deserts.html', recipes=recipes)
    
@app.route('/Pastry')
def Pastry():
    recipes=mongo.db.recipes.find()
    return render_template('Pastry.html', recipes=recipes)
    
@app.route('/QuickBreads')
def QuickBreads():
    recipes=mongo.db.recipes.find()
    return render_template('QuickBreads.html', recipes=recipes)
    
@app.route('/ReducedFat')
def ReducedFat():
    recipes=mongo.db.recipes.find()
    return render_template('ReducedFat.html', recipes=recipes)
    

# This route selects a specific recipe from the database when the specific link for it is selected. It checks for the corrisponding object id in the collection.
@app.route('/recipespage/<recipe_id>', methods=['GET', 'POST'])
def recipespage(recipe_id):
    """Route to show single recipe view page"""
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) #Here you are only finding one!
    all_recipes = mongo.db.recipes.find().limit(4)#Pass them all down to the view and iterate over this and not just 1! hahahahaha
    return render_template('recipes_name.html', recipes=recipes, all_recipes=all_recipes)
	
    
# This route displays the login page 
@app.route('/login')
def login():
    return render_template('Login.html')
    
# This route is used to check what username and password is entered and if it is in the database, it logs the user in. If the user does not exist it informs the user. 
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
    
# This route allows the user to log out when they are done on the site, if they do not log out they remain logged in until they next visit. 
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # Kill session
    return redirect(url_for('index'))

# This route displays the register page   
@app.route('/register')
def register():
    return render_template('register.html')

# This route displays the userpage as well as checks the users and recipes collections
@app.route('/users')
def users():
    users=mongo.db.users.find()
    recipes=mongo.db.recipes.find()
    return render_template('userpage.html', users=users, recipes=recipes)
    
# This route adds the new user to my users collection if they dont exist. If the user does exists then they user gets told they cant use that username
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

# This route checks the recipes collection for the userpage 
@app.route('/recipe_name')
def recipe_name():
    rec=mongo.db.recipes.find()
    return render_template('userpage.html', rec=recipes)


# This route displays the add recipe page and checks the categories and subcategories collections 
@app.route('/add_recipe')
def add_recipe():
    categories=mongo.db.categories.find()
    subcategory=mongo.db.subcategory.find()
    return render_template('addrecipe.html',
    categories=categories, subcategory=subcategory)
    
# This route adds the recipe to the recipes collection if the recipe name does not exist 
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    if request.method == 'POST':
        tasks = mongo.db.recipes
        existing_recipe = tasks.find_one({'name' : request.form['name']})

    # This section is the manual dictionary for the add recipe form. I have added parts to each line so that if something is not entered into the form it adds the next one in the form.get
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
            'description': request.form.get('description'),
            'kcal' : request.form.get('kcal',"unknown"),
            'fat': request.form.get('fat'),
            'saturates': request.form.get('saturates'),
            'carbs': request.form.get('carbs'),
            'sugars': request.form.get('sugars'),
            'fibre': request.form.get('fibre'),
            'protein': request.form.get('protein'),
            'salt': request.form.get('salt'),
            'image_url': request.form.get('image_url'),
            'author': session['name'].title(), #See author now can be added
    		'approval': 'no', # And approval 
        })
        flash('recipe is added to approval list.')
        return redirect(url_for('recipes'))
    flash('Sorry recipe already exists!')
    return redirect(url_for('add_recipe'))
    
# This route displays the admin page. Only the user named Admin can see the link for this page  
@app.route('/admin')
def admin():
    users=mongo.db.users.find()
    recipes=mongo.db.recipes.find()
    return render_template('admin.html', users=users, recipes=recipes)
    
# This route allows the admin to delete a user if needed to
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('admin'))
    
# This route allows the admin to delete a recipe if needed  
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('admin'))
    
# This route allows the admin to set the recipe as approved so that the public can see it. This is a security precaution to prevent inapropriate content being added to the site  
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update_many({"_id": ObjectId(recipe_id)}, {"$set": {"approval": "yes"}})
    return redirect(url_for('admin'))

# This is were the secret key and info for the ip and port is stored
if __name__ == '__main__':
    app.secret_key = 'Hello'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)