from urllib.parse import quote

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

from data.posts import Post
from data_queries.blog_post_queries import BlogPostQueries
from extensions import db
from models.blog_post import BlogPost

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = quote("ashwath@MVN123")
DB_HOST = "localhost"

SQLALCHEMY_DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DB_URI
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

blog_posts = BlogPost()
blog_post_queries = BlogPostQueries()

@app.route("/init")
def init():
    post = Post()
    all_posts = post.get_posts()

    for post in all_posts:
        blog_post_queries.add_cafe(post)

    return render_template("index.html")


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    res = blog_post_queries.get_all_posts()
    print(res)
    posts = res["result"]

    print(f"inside get_all_posts ====> {posts[0]}")
    print(f"posts length = {len(posts)}")
    # for post in posts:
    #     print(post.title)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show-post')
def show_post():
    # TODO: Retrieve a BlogPost from the database based on the post_id
    post_id = request.args.get('post_id')
    print(f"inside show_post ====> {post_id}")

    result = blog_post_queries.get_post_by_id(post_id)
    requested_post = result["result"]
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    with app.app_context():
        print("==================> Creating tables")
        db.create_all()
        print("==================> Finished Creating tables")
    app.run(debug=True, port=5003)
