import os
from flask import url_for, redirect, render_template
from flask_admin import Admin
from flask_login import LoginManager, login_user, logout_user, login_required
from flask import request
from werkzeug.security import check_password_hash
from db import db_add, user_add_in_db
from models import Users, MyModelView, MyAdminIndexView
from app import app, db

# login
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    """
    load user from db
    """
    return Users.query.get(int(user_id))


# admin
admin = Admin(app, name='site', template_mode='bootstrap3', index_view=MyAdminIndexView(), url='/')
# add model in admin
admin.add_view(MyModelView(Users, db.session))


# view
@app.route("/")
def index():
    """
    home page
    """
    return render_template('index.html', title='Home')


@app.route('/login')
def login():
    """
    login page get request
    """
    return render_template('login.html')


@app.route("/login", methods=["POST"])
def login_post():
    """
    login page post request
    """
    # get login_name and password
    login_name = request.form['login']
    password = request.form['password']
    # get user from db by login_name
    user = Users.query.filter(Users.login == login_name).first()
    # check user and password
    if user and check_password_hash(user.password, password):
        # authorization in admin
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login')


@app.route('/logout')
@login_required
def logout():
    """
    logout in admin
    :return:
    """
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    # check availability file db
    if not os.path.exists('instance/blog.db'):
        # add db
        db_add()
        # add user in db
        user_add_in_db('user', '123')
    app.run(debug=True)
