from flask import Flask

app = Flask(__name__)

def fibcalc(arg):
    z = [0]
    a, b = 0, 1
    for i in range(arg):
       a, b = b, a + b
       z.append(a)
    return z

@app.route('/fib/<int:m>')
def fib(m):
    y = int(m)
    ftmp = fibcalc(y)
    return str(ftmp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
