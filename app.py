from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("./blog.db")
c = conn.cursor()


@app.route("/")
def home():
    return render_template("home.html", title="Home | The Pallets Project")


@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects | The Pallets Project")


@app.route("/governance")
def governance():
    return render_template('governance.html', title = 'Governance | The Pallets Project')






if __name__ == "__main__":
    app.run(debug=True)


