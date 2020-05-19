import os
import sys

from flask import url_for
from flask import Flask, redirect, render_template

app = Flask("Flask Test")

@app.route('/')
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="localhost")