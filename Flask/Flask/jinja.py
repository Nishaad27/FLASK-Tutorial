from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<HTML><H1>Welcome to this flask course</H1></HTML"

@app.route("/index")
def index():
    return render_template('index.html')
@app.route("/about")
def abbout():
    return render_template('about.html')

@app.route('/submit',methods = ['GET','POST'])
def sumbit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')
# variable rule
# by default it is String
@app.route('/success/<int:score>')
def score(score):
    return  "The marks you got is" + str(score)

if __name__ == "__main__":
    app.run(debug = True)