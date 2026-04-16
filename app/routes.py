from flask import Blueprint, render_template, request, redirect, session
from dotenv import load_dotenv
import sqlite3
import random
import os

main = Blueprint('main', __name__, template_folder='../templates')

@main.route("/")
def index():
    return render_template("index.html", admin=session.get("admin"))

@main.route("/submit", methods=["POST"])
def submit():

    content = request.form["content"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO posts (content, approved) VALUES (?,0)", (content,))
    conn.commit()

    return redirect("/")

@main.route("/random")
def random_post():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT content FROM posts WHERE approved=1")
    posts = cur.fetchall()

    conn.close()

    if not posts:
        return {"content": "No posts yet"}

    post = random.choice(posts)

    return {"content": post[0]}

@main.route("/posts")
def posts():
    
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT id, content FROM posts WHERE approved=1")

    posts = cur.fetchall()

    return render_template("posts.html", posts=posts, admin=session.get("admin"))

@main.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect("/admin_login")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT id, content FROM posts WHERE approved=0")

    posts = cur.fetchall()

    conn.close()

    return render_template("admin.html", posts=posts)

@main.route("/admin_login", methods=["GET","POST"])
def admin_login():

    if request.method == "POST":

        password = request.form["password"]

        if password == os.getenv("ADMIN_PASSWORD"):
            session["admin"] = True
            return redirect("/admin")

    return render_template("admin_login.html")

@main.route("/approve/<int:id>")
def approve(id):

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("UPDATE posts SET approved=1 WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/admin")

@main.route("/delete/<int:id>")
def delete_post(id):

    if not session.get("admin"):
        return redirect("/")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM posts WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/admin")

@main.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/")