from yoda import app 
from flask import render_template, redirect 
from aluno.form import RegisterForm

@app.route('/login')
def login():
    return 'Olá Aluno'


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('aluno/register.html', form=form)
