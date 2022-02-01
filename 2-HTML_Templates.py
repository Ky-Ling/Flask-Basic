'''
Date: 2021-10-08 18:28:18
LastEditors: GC
LastEditTime: 2021-10-29 22:06:20
FilePath: \Flask\2-HTML_Templates.py
'''
from flask import Flask, render_template

# render_template is gonna allow us grab a HTML file and render that as our web page.
app = Flask(__name__)


# @app.route("/")
# def home():
#     # Just render a HTML file I have created and show that.
#     return render_template("index.html")


# How to show dynamic information on the screen?
@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2)
# It means we will render this HTML file and pass the variable content value of name. So this content in the html file will be
#   replaced with whatever name that we had passed and it will show us the name.


if __name__ == "__main__":
    app.run(debug=True)
