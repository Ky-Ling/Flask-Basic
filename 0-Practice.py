'''
Date: 2021-10-29 21:57:36
LastEditors: GC
LastEditTime: 2021-10-30 19:36:44
FilePath: \Flask\0-Practice.py
'''
from flask import Flask, request, redirect, render_template, url_for, session

app = Flask(__name__)

app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("practice.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login1.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"{user}"
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
