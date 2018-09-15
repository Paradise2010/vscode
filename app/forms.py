from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField("usename",validators=[DataRequired(message="please input usranme")])
    password = PasswordField("password",validators=[DataRequired(message="please input password")])
    remember_me = BooleanField("remember me")
    submit = SubmitField("Login in")