'''
Date: 2021-10-09 19:41:35
LastEditors: GC
LastEditTime: 2021-10-12 14:27:40
FilePath: \Flask\5-Sessions.py
'''
from flask import Flask, render_template, request, url_for, redirect, session
from datetime import timedelta

app = Flask(__name__)

# We have to define the secret key which will be the way that we decrypt and encrypt this data.
app.secret_key = "hello"

# Permanent sessions: we can use the session for longer
# Set up the max time that our session could last for
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index0.html")


# When the user login in, we create a session for them that stores the name and then we can redirect to another page and we
#   don't need to pass parameters, we can access the user name and display it on the screen.
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # It will define this specific session as a permanent session.
        session.permanent = True

        # Get the user information from the login.html
        user = request.form["nm"]

        # Set up some session data based on whatever information they typed in.
        session["user"] = user
        return redirect(url_for("user"))
    else:
        # I wanna check if we are already loginned in, so i just redirect to the user page, otherwise i am just gonna redirect to the
        #   login page.
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    # Get the session information.

    # First, check if there is any information in the session, so i wanna make sure that before i reference that dictionary key.
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        # Redirect back to the login page.

        redirect(url_for("login"))

# There is one thing we should notice: when we close the web browser, my session data is actually deleted from the server which
#   means that if we go back to the user page, we need to create a new session and login in again.


# Actually, if someone logins out the page and you wanna delete all the information associated with their session.
@app.route("/loginout")
def loginout():
    # Remove the data from our session.
    session.pop("user", None)
    return redirect(url_for("login"))

    # Then we have to add something to the login function.


if __name__ == "__main__":
    app.run(debug=True)


# Sessions are temporary, they are stored on the web server and they are just simply there for quick access of infermation
#   between all the different page of your websites.
