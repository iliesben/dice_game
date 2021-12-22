from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/diceGame")

def index():
    return render_template("index.html")
