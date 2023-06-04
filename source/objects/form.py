from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    user = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('PassWord', validators=[DataRequired()])
    submit = SubmitField('Submit')

class User(UserMixin):
    pass