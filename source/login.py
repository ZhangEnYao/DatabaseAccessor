from flask import Blueprint, redirect, render_template, flash, request, session
from flask_login import login_user

from .objects.form import UserForm, User

def verify_user(user_id, password):
    if user_id == 'enyaochang@gmail.com' and password == 'Ph0975578196':
        return True
    return False

EMPTY_STRING = ''

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/login", methods = ['GET', 'POST'])
def login():
    form = UserForm()
    name = EMPTY_STRING
    if form.validate_on_submit():
        user = User()
        user.id = form.user.data
        login_user(user)
        session['user'], *_ = form.user.data.partition('@')
        if verify_user(form.user.data, form.password.data):
            return redirect(request.args.get('next'))
        else:
            flash("[Information] Invalid user or password!")
            return render_template("login.html", form = form, name = name)
    else:
        return render_template("login.html", form = form, name = name)