from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from venv.login.auth.forms import LoginForm, RegistrationForm
from .. import db
from venv.models import users,role

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users = users(id=form.id.data,
                            name=form.name.data,
                            email=form.email.data,
                            roleID=form.roleID.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(users)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = users.query.filter_by(email=form.email.data).first()
        if users is not None and users.verify_password(
                form.password.data):
            # log employee in
            login_user(users)
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))


