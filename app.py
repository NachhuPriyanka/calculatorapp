from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
        a = float(request.args.get('a', 1))
        b = float(request.args.get('b', 1))
        if b == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        return jsonify(result=a / b)

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

