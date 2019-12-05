from flask_wtf import Form 
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField 

class RegisterForm(Form):
    fullname = StringField('Nome Completo', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Nome de usuário', [validators.Required(), validators.Length(min=4, max=25)])
    password = PasswordField('Senha', [validators.Required(), 
                                       validators.EqualTo('confirm', message='As senhas devem ser iguais.'), 
                                       validators.Length(min=4, max=80)])
    confirm = PasswordField('Confirmar senha')
