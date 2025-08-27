from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Usuário:', validators=[DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    username = StringField('Usuário:', validators=[DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(min=6, message='A senha deve ter pelo menos 6 caracteres')])
    submit = SubmitField('Registrar')
