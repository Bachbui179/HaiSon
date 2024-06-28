from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def forward_request(service_url, params):
    response = requests.get(service_url, params=params)
    return response.json(), response.status_code

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    service_url = 'http://localhost:5001/weather'
    return forward_request(service_url, {'city': city})

@app.route('/convert_currency', methods=['GET'])
def currency():
    amount = request.args.get('amount')
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    if not all([amount, from_currency, to_currency]):
        return jsonify({"error": "Amount, from, and to parameters are required"}), 400
    service_url = 'http://localhost:5002/convert_currency'
    return forward_request(service_url, {
        'amount': amount,
        'from': from_currency,
        'to': to_currency
    })

@app.route('/news', methods=['GET'])
def news():
    service_url = 'http://localhost:5003/news'
    return forward_request(service_url, {})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
