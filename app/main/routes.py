from flask import render_template
from flask_login import login_required, current_user
from . import main

@main.route("/")
@main.route("/home")
def index():
    return render_template("main/index.html", title = "Home")

@main.route("/about")
def about():
    return render_template("main/about.html", title = "About")

@main.route("/logged_in")
@login_required
def logged_in():
    username = current_user.username
    return render_template("main/logged_in.html", username = username)