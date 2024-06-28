from flask import Flask, jsonify, request

app = Flask(__name__)

import requests

def get_weather(city):
    api_key = 'a5415a26f5090289b7ff15bd95ee1946'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    weather_data = get_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Could not fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
