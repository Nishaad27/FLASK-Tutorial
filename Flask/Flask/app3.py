from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return "welcome to the index page"

if __name__ == "__main__":
    app.run(debug = True)