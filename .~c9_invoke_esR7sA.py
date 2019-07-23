import os
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'Bakery_Wikipedia'
app.config["MONGO_URI"] = 'mongodb+srv://Argo:LetsL3arn@myfistdb-aslxy.mongodb.net/Bakery_Wikipedia?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    if 'name' in session:
        return 'You are already logged in as ' + session['name']
    
    return render_template('index.html')
    
    
@app.route('/recipes')
def recipes():
    if 'name' in session:
        return 'You are already logged in as ' + session['name']
    
    return render_template('recipes.html')
    
    
@app.route('/login')
def login():
    return render_template('Login.html')
    

@app.route('/find_user', methods=['POST'])
def find_user():
    if request.method == 'POST':
        user = mongo.db.users  #Load your user collection
        existing_user = user.find_one({'name': request.form['name']}) #Check if user already exists
        session['name'] = request.form['name'] #Upon successful registration set the username to the session
        session['logged_in'] = True # Set a indicator to help user later on
        flash('You are now registered')
        return redirect(url_for('index'))
        flash('Sorry username already exists!')
        return redirect(url_for('insert_user'))
        
        
        if session is None:
            return 'No user exists with this name!'
            
        # if request.form['pass'] == 'password' and request.form['name'] == 'users':
        #     session['logged_in'] = True
        #     return session.name
            
    return render_template('index.html', users=mongo.db.users.find())
    
    
    
@app.route('/users')
def users():
    if 'name' in session:
        return 'You are already logged in as ' + session['name']
        
    return render_template('userpage.html', users=mongo.db.users.find())
    
    
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        user = mongo.db.users  #Load your user collection
        existing_user = user.find_one({'name': request.form['name']}) #Check if user already exists
        
        
        if existing_user is None:  #If user doesn't exist then lets register them
            #tasks = mongo.db.users  # This is not needed already done on line 4
            user.insert(request.form.to_dict()) #I'd map the fields manually and not use to_dict() method..
            session['name'] = request.form['name'] #Upon successful registration set the username to the session
            session['logged_in'] = True # Set a indicator to help user later on
            flash('You are now registered')
            return redirect(url_for('index'))
            flash('Sorry username already exists!')
            return redirect(url_for('insert_user'))
	
    return render_template('register.html')

if __name__ == '__main__':
    app.sect
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
