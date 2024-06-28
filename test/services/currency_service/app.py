from flask import Flask, jsonify, request

app = Flask(__name__)

import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = 'dd0488543281b25f4a2f8eac'  # Replace with your actual API key
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(to_currency)
        if rate:
            converted_amount = amount * rate
            return {
                "amount": amount,
                "from": from_currency,
                "to": to_currency,
                "converted_amount": converted_amount
            }
    return None


@app.route('/convert_currency', methods=['GET'])
def currency():
    amount = request.args.get('amount')
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    if not all([amount, from_currency, to_currency]):
        return jsonify({"error": "Amount, from, and to parameters are required"}), 400
    conversion_result = convert_currency(float(amount), from_currency, to_currency)
    if conversion_result:
        return jsonify(conversion_result)
    else:
        return jsonify({"error": "Could not convert currency"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)