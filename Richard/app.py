from flask import current_app as app

from flask import Flask, render_template, request, url_for,redirect, flash, session
import requests, pickle
from github import Github, NamedUser

from .forms import LoginForm, SignUpForm, AuthGitUserForm, UserSettingsForm
from .data_processing import *


clientId = '8b9b835dd53a59b03762'
clientSectet = 'b76d9b1a0c1bfc2a1d9962f396a30a9ea74822bb'
state = 'JSXnC7wwRDpekr6pndyt6qDKxnvbnrvj96xDzhSUrUm7L7kAbjBGe6PwG2tZHVxSQ5m7Lu'
#state is an unguessable string that prevents crsf attacks during github get and post requests

@app.route('/')
def home():
    return render_template('Richard/templates/home.html')


@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    if 'user' in session: #If user has already logged in, just go to dashboard without logging in again
        flash('Already logged in')
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        form_info = request.form
        username, password = form_info['username'], form_info['password']
        if checkPassword(username, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            #if login does not work
            #return redirect(url_for('login_page'))
            flash('Login Unsuccessful', 'error')
    return render_template('Richard/templates/login.html', form=form)
    # return render_template('loginPage.html, form=form')

@app.route('/signup', methods = ['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if form.validate_on_submit():
        form_info = request.form
        username,password,email,phone = form_info['username'], form_info['password'],\
                                        form_info['email'], form_info['phone']

        retypePassword = form_info['retypePassword']
        if retypePassword != password:
            flash("Password's do not match. Please try again.")
        try:
            addUser(username, password, email, phone)
        except:
            flash("Unique constraint has failed. Please try again.")
            return redirect(url_for('signup_page'))
        else:
            session['user'] = username
            return redirect(url_for('dashboard'))
    return render_template('Richard/templates/signUp.html', form=form)

@app.route('/signedUp')
def signedUp():
    return render_template('signedUp.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user' not in session: #if user isn't logged in
        return redirect(url_for('home'))

    if 'access_token' not in session: #if user hasn't signed to github yet
        form = AuthGitUserForm()
        if form.validate_on_submit():
            form_info = request.form
            gitUsername = form_info['username']
            session['git_username'] = gitUsername
            url = get_url(gitUsername) #url is the link to GITHUB authentication portal
            return redirect(url) #redirects user to GITHUB authentication portal
        return render_template('Richard/templates/unauthdashboard.html', form=form)
    return render_template('Richard/templates/dashboard.html', session=session)
    #TODO: setup a nice dashboard

@app.route('/authoriseUser')
def authorise():
    param = request.args #immutable dictionary with parsed contents of query string
    code = param.get('code')
    passedState = param.get('state')
    if passedState != state:
        #the 'state' is just an unguessable random string to prevent CRSF attacks
        #if ths state the GITHUB passed isn't equal to ours, then a CRSF attack has occured
        return render_template('failedAuthentication')

    access_token = get_access_token(code)
    session['access_token'] = access_token
    """TODO: if access tokens are always the same for same user, then we could add
        session['access_token' + session['user']] = access_token
        Or maybe insert access token into database so website will remember
    """
    return redirect(url_for('dashboard'))

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if 'user' not in session:
        return redirect(url_for('home'))

    form = UserSettingsForm()
    if form.validate_on_submit():
        form_info = request.form
        changeDefault(form_info, session['user'])
        flash('Settings has been updated')

    return render_template('Richard/templates/userSettings.html', form=form)

@app.route("/about")
def about():
    if 'user' not in session:
        return redirect(url_for('home'))

    return render_template('Richard/templates/about.html')

@app.route("/logout")
def logout():
    sessionKeys = ('user', 'access_token')
    for key in sessionKeys:
        if key in session:
            session.pop(key, None)
    return redirect(url_for('home'))

def get_url(gitUsername):
    params = {'client_id': clientId,
            'redirect_uri': 'http://127.0.0.1:5000/authoriseUser',
            'login': gitUsername,
            'state': state,
            'scope': 'repo',
            'allow_signup': 'true'}

    requestData = requests.get('https://github.com/login/oauth/authorize', params=params) #get data
    return requestData.url #this is your url that goes to github authorisation
    #return code

def get_access_token(code):
    #don't call this function externally - it is to get access token from authentication form
    data = {'client_id': clientId,
            'client_secret': clientSectet,
            'code': code,
            'state': state,
            'allow_signup': 'true',
            'redirect_uri': 'http://127.0.0.1:5000/authoriseUser'}

    requestData = requests.post('https://github.com/login/oauth/access_token', data=data)
    access_token = str(requestData.content).split('=')[1].split('&')[0]
    return access_token

def access_token():
    if 'access_token' in session:
        return session['access_token']
    return None

# def login_required(func):
#     #doesn't work for some reason - when you log in, and theres a redirect. idk
#     def inner(*args, **kwargs):
#         if 'user' not in session:
#             return redirect(url_for('home'))
#         return func(*args, **kwargs)
#     return inner


if __name__ == "__main__":
    raise Exception("Don't run this file on its own. run main.py from the root directory")
