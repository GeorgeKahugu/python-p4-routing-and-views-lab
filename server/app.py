# !/usr/bin/env python3

from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    count_list='\n'.join(str(i)for i in range(parameter))
    return count_list+'\n'

@app.route('/math/<int:param1>/<string:operation>/<int:param2>')
def math_operation(param1, operation, param2):
    if operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == 'div':
        result = param1/param2
    elif operation == '%':
        result = param1 % param2
    else:
        return 'Invalid operation'
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
 
