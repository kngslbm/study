from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Help(db.Model):
    title = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, default="leader")
    answer = db.Column(db.String, nullable=False, default="")

    def __repr__(self):
        return f'{self.title} Help {self.username}'


with app.app_context():
    db.create_all()
