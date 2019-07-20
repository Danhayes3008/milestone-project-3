import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask.ext.pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Bakery_Wikipedia'

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
    return render_template('Login.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
