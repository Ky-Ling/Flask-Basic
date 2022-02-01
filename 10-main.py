'''
Date: 2021-10-11 20:55:04
LastEditors: GC
LastEditTime: 2021-10-14 10:09:44
FilePath: \Flask\10-main.py
'''
from flask import Flask, render_template
from blueprints import blue


app = Flask(__name__)

# Set up the blueprint from the main flask application.
app.register_blueprint(blue, url_prefix="/admin")


# In this case, we put nothing in the usr_prefix, when we run this file, if we type "/" after the url, are we go to the test page
#   in the main file or go to the home page in the blueprint page?

#   We will go to the home page. Because whenever we register a blueprint, we will look at the url prefix which in this case is
#   blank which means any url we can pass to the blueprint, we will see if anything matches. So in this case, we type "/", we go to
#   blueprint and see something matches, so we will render the home.html. If there is no "/" route in the blueprint file, we will go to test
#   in this mail file.


# Here is another example, we have a url_prefix with "/admin", so what we do is we pass whatever comes after /admin, for example
#   we type "/admin/" this time, we will pass it to the blueprint and we can see we have a route with "/", so we will render the home page. if we have
#   "/admin/test" for example, we will go to the route with "test" in this case.
@app.route("/")
def test():
    return "<h1>This is a test page!</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# How to import the blueprint file and have the blueprint work properly?
# Create a new file as the Python package with nothing inside this Python file (__init__).
# This file allows us to reference the folder name to import modules from it.
# Then change the import information: from admin.blueprint import blue.
