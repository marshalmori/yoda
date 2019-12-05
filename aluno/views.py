from yoda import app 
from flask import render_template, redirect, url_for
from aluno.form import RegisterForm

# @app.route('/login')
# def login():
#     return 'Olá Aluno'


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('aluno/register.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')