'''
Date: 2021-10-08 14:09:58
LastEditors: GC
LastEditTime: 2021-10-29 21:56:14
FilePath: \Flask\1-Basic.py
'''


from flask import Flask, redirect, url_for

# Create an instance of a flask web application.
app = Flask(__name__)


# Define the pages that will be on my website.
# Define how we can access this specific page. Inside the (), we will define the path that we want to use to get to this function.
#   If we only type "/", it means that whenever we go to our default domain, whatever that might be, it will automatically sent
#   us the home page.

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
# We will define a home page and this function will be displayed on the page.
def home():
    # Add inline HTML when we are returning it from a function.
    return "Hello, this is a home web page!"


# Inside the(), Whenever I type something, it's gonna grab that value and pass it to my function as a parameter.
@app.route("/<name>")
def user(name):
    return f"Hello {name}"


# How to redirect different pages from our code?
# We have to import redirect and url-for, they allow me to actually return a redirect from a specific function.
@app.route("/admin")
def admin():
    # Inside the (), we can put the name of the function that we are going to be redirecting to.
    return redirect(url_for("user", name="Admin!"))

# When I go to the /admin page, it's gonna return the url for user and it is gonna pass through the argument
#   Admin, and it will print "Hello Admin"


# Run this app.
if __name__ == "__main__":
    app.run(debug=True)
