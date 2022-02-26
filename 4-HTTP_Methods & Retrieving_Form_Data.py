'''
Date: 2021-10-09 14:21:32
LastEditors: GC
LastEditTime: 2022-02-26 14:43:35
FilePath: \Flask\4-HTTP_Methods & Retrieving_Form_Data.py
'''
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# The default method is GET
@app.route("/")
def home():
    return render_template("index0.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    # How can we check whether we reach this page with get request or post request?
    if request.method == "POST":
        # We will get the information that was from that name box and then send to the user page where we
        #   can display the user's name.
        user = request.form["nm"]
        
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

# We have this login page and once we logged in, we can get the user name and then we can redirect them to a page that show their name.

@ app.route("/<usr>")
def user(usr):
    return f"<h1>The user name is {usr}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# GET: The most common insecure way of getting or sending information to a website or a client depending on the way of this information is
#   going.

# POST: It's the secure way of doing these things. It will sent secure information that encrypted that you can't see from either
#   ends and is not stored on the actual web server.
