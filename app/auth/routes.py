from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from .. import db
from ..Forms import LoginForm, SignUpForm
from . import auth
from ..models import User

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    next_page = request.args.get("next")
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        flash("You have been logged in", "success")
        return redirect(next_page or url_for("main.logged_in"))
    return render_template("auth/login.html", title = "Login page" , form = form)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Account created successfully", "success")
        return redirect(url_for("main.index"))
    return render_template("auth/signup.html", title = "Login page", form = form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("main.index"))