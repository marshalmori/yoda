from yoda import db 

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    is_aluno = db.Column(db.Boolean)

    def __init__(self, fullname, email, username, password, is_aluno=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_aluno = is_aluno

    def __repr__(self):
        return '<Aluno %r>' %self.username

