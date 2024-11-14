from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route("/")
def index():  
    return "Hello!"

@app.route('/calc')
def calculate():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b
        return jsonify({'result': result}),200
    except ValueError:
        return jsonify({'error': "Invalid input"}), 400


def sum(a,b):
    return a+b

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0') 