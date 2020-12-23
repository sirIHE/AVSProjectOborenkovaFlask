from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from models.lecturer import Lecturer
from managers.DatabaseManager import DatabaseManager
# from flask_sqlalchemy import SQLAlchemy
# from peewee import *
from extensions import db

db_manager = DatabaseManager(db)

addLecturer = Blueprint('addLecturer', __name__,
                template_folder='templates',
                static_folder='static')


@addLecturer.route('/addLecturer')
def index3():
	return render_template('addLecturer.html')


@addLecturer.route('/addLecturer', methods=['post', 'get'])
def addLec():
    message = ''
    if request.method == 'POST':
        last_name = request.form.get('last_name')
        name = request.form.get('name')
        surname = request.form.get('surname')

    if last_name and name and surname:
        message = "Correct data"
        db_manager.add_lecturer(name=name, last_name=last_name, surname=surname)
        # conn = SqliteDatabase('app.db')
        # lecturer = Lecturer(name=name, last_name=last_name, surname=surname)
        # lecturer.save()
    else:
        message = "Wrong data"

    return render_template('addLecturer.html', message=message)




# def index2():
# 	return render_template('addlecturer.html',groups=Group.query.all())