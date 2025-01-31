from flask import Flask, render_template, redirect, url_for, request, session

from datetime import timedelta

#creating an instance of class
app = Flask(__name__)
app.secret_key = "xyz"
app.permanent_session_lifetime = timedelta(days=1)

#home page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}<h1/>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "_main_":
    app.run()
from flask import Flask, render_template, redirect, url_for, request, session

from datetime import timedelta

#creating an instance of class
app = Flask(__name__)
app.secret_key = "xyz"
app.permanent_session_lifetime = timedelta(days=1)

#home page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}<h1/>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "_main_":
    app.run()