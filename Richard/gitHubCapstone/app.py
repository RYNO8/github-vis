from flask import Flask
import sqlite3

from flask import Flask, render_template, request, url_for,redirect, flash
from flask_bootstrap import Bootstrap
from forms import LoginForm, SignUpForm
from data_processing import *
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin


app = Flask(__name__)
app.secret_key="github1203"
bootstrap = Bootstrap(app)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'home'
#this redirects to 'home' function when user tries to access page without logging in

#Next time, use sessions for login page


class User(UserMixin):
    #Note: the get_id() method in UserMixin gets it from self.id
    #Very bad approach but i have no idea what i am doing
    def __init__(self,username = None, userId = None):
        if userId == None:
            self.username = username
            self.id = getUserId(self.username)
        else: # if username = None
            self.id = userId
            self.username = getUsername(self.id)



@login_manager.user_loader
def load_user(userId):
    user = User(userId = userId)
    return user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        form_info = request.form
        username, password = form_info['username'], form_info['password']
        user = User(username = username) #kind of brute forced it so the user has the MIXIN attributes
        if checkPassword(username, password):
            login_user(user, remember=form.remember.data)
            #if login works
            return redirect(url_for('dashboard'))
        else:
            #if login does not work
            #return redirect(url_for('login_page'))
            flash('Login Unsuccessful')
    return render_template('login.html', form=form)
    # return render_template('loginPage.html, form=form')

@app.route('/signup', methods = ['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if form.validate_on_submit():
        form_info = request.form
        username,password,email,phone = form_info['username'], form_info['password'],\
                                        form_info['email'], form_info['phone']
        try:
            addUser(username,password,email,phone)
            return render_template('signedUp.html')
        except:
            return 'hello'
    return render_template('signUp.html', form=form)

@app.route('/signedUp')
def signedUp():
    return render_template('signedUp.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
    #TODO: setup a nice dashboard


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

