'''
Date: 2021-10-09 13:41:08
LastEditors: GC
LastEditTime: 2021-10-09 14:08:07
FilePath: \Flask\3-Template_Inheritance.py
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index1.html", content="testing")


if __name__ == "__main__":
    app.run(debug=True)
