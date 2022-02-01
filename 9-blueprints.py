'''
Date: 2021-10-11 20:47:36
LastEditors: GC
LastEditTime: 2021-10-11 21:30:58
FilePath: \Flask\9-Blueprints.py
'''
from flask import Blueprint, render_template

# Set up the blueprint
blue = Blueprint("blue", __name__, static_folder="static",
                 template_folder="templates")

# Next just set up the routes and functions, do not need to run this Python file, we just use something from this file.


@blue.route("/home")
@blue.route("/")
def home():
    return render_template("home.html")


@blue.route("test")
def test():
    return "<h1>Test for url-prefix!</h1>"


# Blueprints allow us to divide up our application into separate Python files where we can pass specific views and render templats
#   from different areas of our application.

# Create a new folder called admin, and move the static and templates folders and blueprint file into this admin folder.
#   so that we can use this mini app in the other main application.


