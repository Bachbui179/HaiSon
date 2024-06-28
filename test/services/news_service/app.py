from flask import Flask, jsonify

import requests

def get_news():
    api_key = 'fcc394e7b7f6416681d3f3a95447392a'  # Replace with your actual API key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = [{
            "source": article["source"]["name"],
            "author": article["author"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "urlToImage": article["urlToImage"],
            "publishedAt": article["publishedAt"],
            "content": article["content"]
        } for article in data["articles"]]
        return {"articles": articles}
    else:
        return None


app = Flask(__name__)

@app.route('/news', methods=['GET'])
def news():
    headlines = get_news()
    if headlines:
        return jsonify(headlines)
    else:
        return jsonify({"error": "Could not fetch news"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)
