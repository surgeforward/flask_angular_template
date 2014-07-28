from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

__all__ = ['RegisterForm', 'LoginForm', 'RoleForm']


class RegisterForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])


class LoginForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])


class RoleForm(Form):
    name = TextField('Name', validators=[Required(), Email()])
    description = TextField('Description', validators=[Required()])

