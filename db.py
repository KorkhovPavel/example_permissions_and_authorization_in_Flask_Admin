from werkzeug.security import generate_password_hash
from app import app, db
from models import Users


def db_add():
    """
    create db
    """
    with app.app_context():
        db.create_all()


def user_add_in_db(username, password):
    """
    Add user in db
    Password is hash
    """
    hash_psw = generate_password_hash(password)
    u = Users(login=username, password=hash_psw)
    with app.app_context():
        db.session.add(u)
        db.session.commit()
