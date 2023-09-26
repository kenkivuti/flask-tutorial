from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/home")
def hello():
    return "software development"

@app.route("/contact us")
def contact():
    return "for more info: contact me at 0723208424"
app.run()