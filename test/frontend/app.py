from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_GATEWAY_URL = 'http://localhost:5000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    return render_template('weather.html')
    
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    response = requests.get(f'{API_GATEWAY_URL}/weather', params={'city': city})
    weather_data = response.json()
    return render_template('weather.html', weather=weather_data)

@app.route('/currency', methods=['GET'])
def currency():
    return render_template('currency.html')

@app.route('/convert_currency', methods=['POST'])
def convert_currency():
    amount = request.form.get('amount')
    from_currency = request.form.get('from_currency')
    to_currency = request.form.get('to_currency')
    response = requests.get(f'{API_GATEWAY_URL}/convert_currency', params={
        'amount': amount,
        'from': from_currency,
        'to': to_currency
    })
    conversion_result = response.json()
    return render_template('currency.html', conversion=conversion_result)



@app.route('/news', methods=['GET'])
def get_news():
    response = requests.get(f'{API_GATEWAY_URL}/news')
    news_data = response.json()
    return render_template('news.html', news=news_data)

@app.route('/food', methods=['GET'])
def food_order():
    return render_template('404_not_found.html')


if __name__ == '__main__':
    app.run(debug=True, port=5004)

