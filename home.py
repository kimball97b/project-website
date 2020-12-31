from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World - <h1>Home<h1>"

app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__=='__main__':
    app.run()
