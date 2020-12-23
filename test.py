from managers.DatabaseManager import DatabaseManager

from app import db
from models.lecturer import Lecturer
from models.schedule import Schedule


db_manager = DatabaseManager(db)

db_manager.add_interval(interval='9:30 - 11:05')
db_manager.add_interval(interval='11:20 - 12:55')
db_manager.add_interval(interval='13:10 - 14:45')
db_manager.add_interval(interval='15:25 - 17:00')

db_manager.add_group(name='БФИ1801')

db_manager.add_subject(subject_name="Архитектуры вычислительных систем")
db_manager.add_subject(subject_name="Операционные системы")
db_manager.add_subject(subject_name="Основы ИБК")
db_manager.add_subject(subject_name="Основы информационной безопасности")
db_manager.add_subject(subject_name="Сетевые технологии")
db_manager.add_subject(subject_name="РиСПСиИТ")
db_manager.add_subject(subject_name="Разработка КПО")
db_manager.add_subject(subject_name="Элективные дисц. по физ. культуре")

db_manager.add_lecturer(name='Тимур', last_name='Фатхулин', surname='Джалилевич')
db_manager.add_lecturer(name="Владимир", last_name='Владимиров', surname='Львович')
db_manager.add_lecturer(name="Светлана", last_name='Королева', surname='Анатольевна')
db_manager.add_lecturer(name="Алексей", last_name='Смирнов', surname='Эдуардович')
db_manager.add_lecturer(name="Алексей", last_name='Руднев', surname='Николаевич')
db_manager.add_lecturer(name="Михаил", last_name='Городничев', surname='Геннадьевич')
db_manager.add_lecturer(name="Татьяна", last_name='Королькова', surname='Валерьевна')
db_manager.add_lecturer(name="Наталья", last_name='Трубникова', surname='Владимировна')

