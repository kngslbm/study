from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Help(db.Model):
    password = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    context = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.title} Help {self.username}'


with app.app_context():
    db.create_all()
