from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():  
    return "Hello!"

@app.route("/calc")
def calculate(): 
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        result = sum(a,b)
        return str(result)
    except ValueError:
        return "Invalid input. Please provide integers for 'a' and 'b'."


def sum(a,b):
    return a+b

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0') 