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
@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')
@app.route('/submit',methods = ['GET','POST'])
def sumbit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')
if __name__ == "__main__":
    app.run(debug = True)