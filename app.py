import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.interval import Interval
from models.group import Group
from models.schedule import Schedule
from models.lecturer import Lecturer
from models.subject import Subject
from flask import request


from Routes.Lecturers import lecturers
from Routes.Groups import groups
from Routes.addLecturer import addLecturer
from Routes.addNote import addNote
from Routes.addGroup import addGroup
from Routes.addSubject import addSubject

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(groups)
app.register_blueprint(addLecturer)
app.register_blueprint(addNote)
app.register_blueprint(addGroup)
app.register_blueprint(addSubject)

if __name__ == "__main__":
    app.run()