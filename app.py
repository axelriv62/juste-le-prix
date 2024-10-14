from flask import Flask, jsonify, request
from APIRequest import get_data

app = Flask(__name__)

@app.route('/api/product', methods=['GET'])
def product_info():
    code = request.args.get('code')
    data = get_data(code)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)