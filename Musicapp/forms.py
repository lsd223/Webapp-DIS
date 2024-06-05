from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class UserSignupForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), 
                                        Length(min=2, max=20)])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), 
                            Length(min=2, max=50)])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
