#Creating forms using wtfForms.  Create a class of the requried data.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class Form(FlaskForm): #Don't forget to inherit FlaskForm, see forms.html to display form.
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Login(FlaskForm): #Don't forget to inherit FlaskForm, see forms.html to display form.
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')

#The validators will display errors on your website live (see forms.html) 