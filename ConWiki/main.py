from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()
