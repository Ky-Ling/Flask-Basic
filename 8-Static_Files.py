'''
Date: 2021-10-11 20:08:19
LastEditors: GC
LastEditTime: 2021-10-11 20:25:56
FilePath: \Flask\8-Static_Files.py
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
