import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt


app = Flask(__name__)
username = session['name']


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
        users = mongo.db.users
        session = users.find({'name': request.form['name']})
        
        if session is None:
            return 'No user exists with this name!'
            
        if request.form['pass'] == 'password' and request.form['name'] == 'users':
            session['logged_in'] = True
            return session['name']
    
    return render_template('userpage.html', users=mongo.db.users.find())
    
    
    
@app.route('/users')
def users():
    if 'name' in session:
        return 'You are already logged in as ' + session['name']
        
    return render_template('userpage.html', users=mongo.db.users.find())
    
    
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find({'name': request.form['name']})
        
       
        
        if existing_user is None:
            tasks = mongo.db.users
            tasks.insert_one(request.form.to_dict())
            return redirect(url_for('index'))
            
        return 'That username already exists!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
