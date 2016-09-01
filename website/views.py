from website import app
from flask import Flask, session, g, render_template


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/neimu/')
def neimu():
    return render_template("neimu.html")


@app.route('/dashiji/')
def dashiji():
    return render_template("dashiji.html")


@app.route('/facai/')
def facai():
    return render_template("facai.html")


@app.route('/jiaru/')
def jiaru():
    return render_template("jiaru.html")
