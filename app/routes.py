from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app

from app.forms import LoginFrom,RegistrationForm
from app.models import User



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/login'))
   
    form = LoginFrom()
 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None and user.check_password(form.password.data):
            flash("Invalid input data")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        newuser = User(username=form.username.data, password=password_hash)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('/login'))
    return render_template("register.html",form=form)