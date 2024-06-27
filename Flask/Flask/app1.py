from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this Amazing flask course this should be an amazing course"

if __name__ == "__main__":
    app.run(debug = True)
## this debug parameter updates the server without having to manually restarting it