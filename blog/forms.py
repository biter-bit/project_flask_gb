from wtforms import Form, StringField, validators, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from flask_wtf import FlaskForm


class UserBaseForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Username", [validators.DataRequired()],)
    email = StringField("Email Adress", [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, max=200),
    ], filters=[lambda data: data and data.lower()],)


class RegisterForm(UserBaseForm):
    password = PasswordField("New Password", [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Passwords must match"),
    ],)
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()], )
    password = PasswordField("Password", [validators.DataRequired()], )
    submit = SubmitField("Login")


class CreateArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
    submit = SubmitField('Publish')
    tags = SelectMultipleField("Tags", coerce=int)