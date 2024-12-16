from ICT import app, db, bcrypt
from flask import redirect, request,render_template,flash,url_for
from ICT.forms import Form, Login
from ICT.models import User
from flask_login import login_user, current_user, logout_user, login_required

#displays all the current users that have been created and added to the database
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)
#grabs user id from index.html link.
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id) #Grabs specific user from database
    user.username = "changed" #db.session.delete() deltes user instead of making a change
    db.session.commit()
    flash("Your user has been deleted", 'success')
    return redirect(url_for('index'))

#import form class from forms.py
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Form()
    if(request.method =='POST'): #if getting a post request it means user hit the submit button
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, password=hashed_password) #grabs data from form and creates user object
            db.session.add(user)
            db.session.commit() #adds to database
            flash('You have Signed UP!!', 'success')
            return redirect(url_for('index'))
        else:
            flash("sign up failed, check errors", 'danger')
    return render_template('forms.html', form=form) #this is passing in the form for the html document to read.


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if(request.method =='POST'): 
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
            flash('You have Logged in!!', 'success')
            return redirect(url_for('index'))
        else:
            flash("sign up failed, check user or password", 'danger')
    return render_template('login.html', form=form) 

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", 'success')
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users = users, title="users")