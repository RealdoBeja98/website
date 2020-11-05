from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

posts = [
    {
        'title': 'Version 8.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 7.1.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 8.0 and will support Python 3.6 and<br> newer.'
        
    },
    {
        'title': 'Install or Upgrade',
        'content': 'Install from PyPI with pip:',
        'installation': 'pip install -U Werkzeug'
    }
]

@app.route("/")
def home():
    return render_template("home.html", title="Home | The Pallets Project")


@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects | The Pallets Project")


@app.route("/governance")
def governance():
    return render_template("governance.html", title="Governance | The Pallets Project")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog | The Pallets Project", posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
    
