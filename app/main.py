import os
from flask import Flask, render_template

app = Flask(__name__)

def fibcalc(arg):
    z = [0]
    a, b = 0, 1
    for i in range(arg):
       a, b = b, a + b
       z.append(a)
    return z


@app.route("/")
def main():
  return render_template('index.html')

@app.route('/v1/fib/<int(max=1000):m>')
def fib(m):
    y = int(m)
    ftmp = fibcalc(y)
    return str(ftmp)

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
