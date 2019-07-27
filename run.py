import os
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    
    
    
@app.route('/users')
def users():
    
    return render_template('userpage.html', users=mongo.db.users.find(),
    author=mongo.db.author.find())
    
    
@app.route('/register')
def register():
    return render_template('register.html')


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
    
    
@app.route('/recipe_name/<name_id>')
def recipe_name(name_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(name_id)})
    return render_template('userpage.html', task=the_recipe)
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find(),
    subcategory=mongo.db.subcategory.find())
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    tasks = mongo.db.recipes
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.secret_key = 'Hello'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
