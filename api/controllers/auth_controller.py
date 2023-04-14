from api import app
from flask import session, redirect, url_for


@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("find_products"))
    return redirect(url_for("find_users"))


@app.route("/login/<user_id>")
def login(user_id):
    session["user_id"] = user_id
    return redirect(url_for("find_products"))


@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect(url_for("find_users"))
