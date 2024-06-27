from flask import Flask,render_template,request
app = Flask(__name__)
'''
{{}} expression to print out put in html
{% %} conditions , for loops
{#...#} this is for comments 
'''

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
    res = ""
    if score >=50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html',results = res)

@app.route('/success_res/<int:score>')
def success(score):
    res = ""
    if score >=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score':score,"res":res}

    return render_template('result1.html',results = exp)
## using if condition
@app.route('/success_if/<int:score>')
def success_2(score):
    return render_template('result2.html',results = score)


if __name__ == "__main__":
    app.run(debug = True)