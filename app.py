from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    

 
posts = [
    {
        'title': 'Version 8.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 7.1.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 8.0 and will support Python 3.6 and<br> newer.'
        
    },
    {
        'title': 'Install or Upgrade',
        'content': 'Install from PyPI with pip:<br> <div class="installation"><ul><li>Drop support for Python 3.4. This will be the last version to support Python 2.7 and 3.5.</li><li>Multiple fixes in low-level Windows compatibility code.</li></ul></div>'
       
    },
    {
        'title': 'Donate to Support Pallets',
        'content': 'The Pallets organization accepts donations as part of the non-profit Python<br> Software Foundation (PSF). Donations through the PSF support our efforts to<br> maintain the projects and grow the community.'
    },
    {
        'title': 'Version 2.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 1.0.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 2.0 and will support Python 3.6 and<br> newer.'
    },
    {
        'title': 'Version 8.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 7.1.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 8.0 and will support Python 3.6 and<br> newer.'
        
    },
    {
        'title': 'Install or Upgrade',
        'content': 'Install from PyPI with pip:<br> <div class="installation"><ul><li>Drop support for Python 3.4. This will be the last version to support Python 2.7 and 3.5.</li><li>Multiple fixes in low-level Windows compatibility code.</li></ul></div>'
       
    },
    {
        'title': 'Donate to Support Pallets',
        'content': 'The Pallets organization accepts donations as part of the non-profit Python<br> Software Foundation (PSF). Donations through the PSF support our efforts to<br> maintain the projects and grow the community.'
    },
    {
        'title': 'Version 2.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 1.0.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 2.0 and will support Python 3.6 and<br> newer.'
    },
    {
        'title': 'Version 8.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 7.1.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 8.0 and will support Python 3.6 and<br> newer.'
        
    },
    {
        'title': 'Install or Upgrade',
        'content': 'Install from PyPI with pip:<br> <div class="installation"><ul><li>Drop support for Python 3.4. This will be the last version to support Python 2.7 and 3.5.</li><li>Multiple fixes in low-level Windows compatibility code.</li></ul></div>'
       
    },
    {
        'title': 'Donate to Support Pallets',
        'content': 'The Pallets organization accepts donations as part of the non-profit Python<br> Software Foundation (PSF). Donations through the PSF support our efforts to<br> maintain the projects and grow the community.'
    },
    {
        'title': 'Version 2.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 1.0.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 2.0 and will support Python 3.6 and<br> newer.'
    },
    {
        'title': 'Version 8.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 7.1.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 8.0 and will support Python 3.6 and<br> newer.'
        
    },
    {
        'title': 'Install or Upgrade',
        'content': 'Install from PyPI with pip:<br> <div class="installation"><ul><li>Drop support for Python 3.4. This will be the last version to support Python 2.7 and 3.5.</li><li>Multiple fixes in low-level Windows compatibility code.</li></ul></div>'
       
    },
    {
        'title': 'Donate to Support Pallets',
        'content': 'The Pallets organization accepts donations as part of the non-profit Python<br> Software Foundation (PSF). Donations through the PSF support our efforts to<br> maintain the projects and grow the community.'
    },
    {
        'title': 'Version 2.0 Coming Soon',
        'content': 'As outlined in Ending Python 2 Support, 1.0.x will be the last version to support<br> Python 2.7 and 3.5. The next version will be 2.0 and will support Python 3.6 and<br> newer.'
    }
]
db.create_all()
for posts_in_blog in posts:
    title_from_dic = posts_in_blog.get("title")
    content_from_dic = posts_in_blog.get("content")
    print(title_from_dic)
    inserting_into_table = Post(title = title_from_dic, content = content_from_dic) 
    db.session.add(inserting_into_table)
    db.session.commit()




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
    
