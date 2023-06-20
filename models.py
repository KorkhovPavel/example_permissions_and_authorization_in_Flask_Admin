from flask import request, redirect, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_login import UserMixin, current_user
from app import db


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), nullable=False)


class MyModelView(sqla.ModelView):

    def is_accessible(self):
        """
        check authorization
        """
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        """
        redirect (if not authorization)
        """
        return redirect(url_for('index', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        """
        check authorization
        """
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        """
        redirect (if not authorization)
        """
        return redirect(url_for('index', next=request.url))
