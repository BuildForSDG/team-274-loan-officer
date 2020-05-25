# set up  db in __init__.py under my projects folder

from project import db, login_manager,app


db.create_all()
