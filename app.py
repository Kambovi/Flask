from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route("/welcome")
def welcome():
    return "<h2>welcome to flask page</h2>"


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")
if __name__== '__main__':
    app.run(debug=True)