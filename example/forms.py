from flask import Flask, redirect, render_template

from data import db_session
from data.db_session import create_session, global_init
from data.users import User
from data.jobs import Jobs
from forms.login_form import LoginForm

from flask_login import login_user, LoginManager, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_magager = LoginManager()
login_magager.init_app(app)


@login_magager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    return user


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        sess = db_session.create_session()
        user = sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/index")

    return render_template("login.html", form=form)


@app.route("/index")
def index():
    return render_template("index.html", current_user=current_user)


def main():
    db_session.global_init("db/mars_explorer.db")
    sess = db_session.create_session()
    user = User()
    user.email = "admin@gmail.com"
    user.name = "qwer"
    user.surname = "qwer"
    user.set_password("12345678")
    sess.add(user)
    sess.commit()
    app.run()


if __name__ == '__main__':
    main()
