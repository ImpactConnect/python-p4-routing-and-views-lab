#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text) 
    return f"<h2>{text}</h2>"

@app.route('/count<int:num>')
def count(num):
    for i in range(0, num + 1):
        return f"{i}\n"
    
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")    
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 // num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation."

    return f"<h1>{num1} {operation} {num2} = {result}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
