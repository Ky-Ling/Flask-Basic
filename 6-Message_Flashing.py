'''
Date: 2021-10-10 09:46:08
LastEditors: GC
LastEditTime: 2022-02-26 15:01:28
FilePath: \Flask\6-Message_Flashing.py
'''

from flask import Flask, render_template, request, url_for, redirect, session, flash


app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("index0.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        # Post request
        user = request.form["nm"]

        flash("Login in successfully!!")
        
        # Set up the session
        session["user"] = user

        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already login in!!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not login in!!")
        return redirect(url_for("login"))


@app.route("/loginout")
def loginout():

    # We can check if we have a user in the session and only if we do then we will say you have been logged out.
    if "user" in session["user"]:
        user = session["user"]
        # When we log out, we can go to the loginout page but then it pops our session and redirects our back to the login page.
        #   So on the login page, we wanna show logged out successfully.
        flash(f"You have been logged out!! {user}", "info")
        # And then we have to go to login.html file to write some jinja code inside the block content to display all the messages that come up.

        # So we can display the name and tell them they have been logged out but only if we have a user in the session.
    session.pop("user", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)


# Message flashing is showing some kind of information form the previous page on the next page when something happends on the GUI.

# We have to import flash function and we can use this function to display or post the message that are be flashed and then from
#   different pages we can decide where we want to flash these.
