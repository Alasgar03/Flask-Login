from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginFrom(FlaskForm):
    username = StringField('Username',
     validators=[DataRequired(), Length(min = 3, max =20)]
    )
    password = PasswordField(
        'Password',
        validators =[DataRequired()]
    )
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
     validators=[DataRequired(), Length(min = 3, max =20)]
    )
    password = PasswordField(
        'Password',
        validators =[DataRequired()]
    )
    confirm_password = PasswordField('Confirm Password', 
    validators=[DataRequired(),EqualTo("password")])
    sumbit = SubmitField("Sign Up")