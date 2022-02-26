'''
Date: 2021-10-10 13:08:03
LastEditors: GC
LastEditTime: 2022-02-26 15:20:36
FilePath: \Flask\7-Using_SQLAlchemy_Database.py
'''
from flask import Flask, redirect, request, flash, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hello"

# Set up a database object
db = SQLAlchemy(app)

# Define a class which represents this user object in the database.
class users(db.Model):
    # Define the properties that we are gonna save
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index0.html")


@app.route("/view")
def view():
    # Pass all the user's database object. Get all of the users and pass the object to the view.html and display all the information on the screen.
    return render_template("view.html", values=users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        
        # Get the information the user typed
        user = request.form["nm"]
        
        # Set up the session
        session["user"] = user

        # Query and grab the information from our database.
        found_user = users.query.filter_by(name=user).first()
        
        if found_user:
            # Grab the user's email and store that in the session so that when we go to next page and we can see that.
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            
            # Add this usr model to the database
            db.session.add(usr)
            db.session.commit()

        flash("Login in successfully!!!")
        return redirect(url_for("user"))

    else:
        if "user" in session:
            flash("Already loginmed in!!!")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        # Check the current method if the user in this session
        if request.method == "POST":
            
            # Grab the email from the email field and set up the session for the email
            email = request.form["email"]
            session["email"] = email

            # When they post their email, what we wanna do is change that specific user's email
            found_user = users.query.filter_by(name=user).first()

            if found_user:
                session["email"] = email
            
            db.session.commit()
            flash("Email was saved!!!")
        else:
            # Get the email from the session
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not login in!!")
        return redirect(url_for("login"))


@app.route("/loginout")
def loginout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out!!{user}", "info")
        
    session.pop("user", None)
    session.pop("email", None)
    
    return redirect(url_for("login"))


if __name__ == "__main__":
    # Create this database if it does not already exist
    db.create_all()
    print("Database have been created!")
    app.run(debug=True)

# How can we save user specific information?
