from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message="This field requires a valid email address with @.")])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, message="Password minium 8 characters")])
    submit = SubmitField(label='Log In')