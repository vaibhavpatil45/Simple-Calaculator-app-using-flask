from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operation):
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            result = "Invalid operation"
        return result
    except Exception as e:
        return "Error"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate_result():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = calculate(num1, num2, operation)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
