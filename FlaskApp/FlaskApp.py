from flask import Flask, render_template, request
app = Flask(__name__)


# From Browser: http://127.0.0.1/add?num1=2&num2=3

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hello', methods=['POST','GET'])
def helloWorld():
    if request.method == 'GET':
        return "Hello World"
    if request.method == 'POST':
        return 'Namaste'

@app.route('/add')
def addRoute():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    Sum_result = str(n1+n2)
    return render_template("output.html", sum=Sum_result, num1=n1,num2=n2)

@app.route('/mult')
def multRoute():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    result = n1*n2
    return str(result)

@app.route('/sub')
def subRoute():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    result = n1-n2
    return str(result)

@app.route('/div')
def divRoute():
    n1 = float(request.args.get("num1"))
    n2 = float(request.args.get("num2"))
    result = n1/n2
    return str(result)

'''
@app.route('/', methods=['POST'])
def result():
    num1 = request.form.get("num1", type=int, default=0)
    num2 = request.form.get("num2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = num1 + num2
    elif(operation == 'Subtraction'):
        result = num1 - num2
    elif(operation == 'Multiplication'):
        result = num1 * num2
    elif(operation == 'Division'):
    	if(num1==0 and num2==0):
    		result = 0
    	else:
        	result = num1 / num2
    else:
        result = 0
    entry = result
    return render_template('index.html', entry=entry)
'''

if __name__ == "__main__":
    app.run(debug=True,port=80)
