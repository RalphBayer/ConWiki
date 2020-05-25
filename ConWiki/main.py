from flask import Flask, render_template, request, make_response, jsonify
from article_manager import *

app = Flask(__name__)

# ---------------------------- Functions for Flask ---------------------------- #

@app.route("/")
def main():
    return homepage()

@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/create.html")
def create():
    return render_template("create.html")

@app.route("/help.html")
def help():
    return render_template("help.html")

@app.route("/create.html/post_json", methods=['POST'])
def json():
    req = request.get_json()
    create_article(req)
    return make_response(jsonify({"message":"JSON received"}), 200)

# ---------------------------- Starts the flask server ---------------------------- #

if __name__ == "__main__":
    app.run()
