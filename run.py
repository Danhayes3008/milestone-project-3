import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Bakery_Wikipedia'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
    
@app.route('/recipes')
def recipes():
    return render_template('recipes.html')
    
@app.route('/login')
def login():
    if 'username' in session:
        return 'you are logged in as ' + session['username']
    return render_template('Login.html')
    
@app.route('/users')
def users():
    return render_template('userpage.html')
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('userpage.html'))
            
        return 'That username already exists!'
    
    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
