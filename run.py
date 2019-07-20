import os
from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, UserMixin
import bcrypt

app = Flask(__name__)

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
