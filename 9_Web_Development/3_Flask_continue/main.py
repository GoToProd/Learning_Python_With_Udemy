import os
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def start_page():
    return "Hi my dear friend!"

@app.route("/user/<username>")
def show_user(username):
    return f"User {escape(username)}"

@app.route("/post")
def show_post():
    return render_template("recept.html")

@app.route("/id/<path:username>")
def show_id(username):
    return f'Name your user {username}'

@app.route("/projects/")
def projects():
    return render_template("work.html")

@app.route("/projects/recept")
def projectsrecept():
    return render_template("recept.html")

@app.route("/sname/<path:username>/<str>/")
def sname (username, str):
    return (f'Name your is {username} and {str}')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, use_debugger=True)
