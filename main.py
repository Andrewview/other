from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def indexView():
    return render_template('start.html', data = 0)

@app.route('/new1')
def new1View():
    return render_template('cooperation.html', data = 1)

@app.route('/new2')
def new2View():
    return render_template('about.html', data = 2)

@app.route('/registration')
def new3View():
    return render_template('register.html', data = 3)








if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')