# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# # OpenWeatherMap API Key (Replace with your actual key)
# API_KEY = " "
# BASE_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f2687bb3ba514ebdb8a3b90a60c91a43"

# # List of major cities in Pakistan
# CITIES = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar", "Multan"]

# @app.route('/weather', methods=['GET'])
# def get_weather():
#     city = request.args.get('peshawar', default="Karachi")  # Default to Karachi if no city is provided

#     if city not in CITIES:
#         return jsonify({"error": "City not found. Choose from: Karachi, Lahore, Islamabad, Quetta, Peshawar, Multan"}), 400

#     # API request to OpenWeatherMap
#     url = f"{"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f2687bb3ba514ebdb8a3b90a60c91a43"}?q={"peshawar"},PK&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     data = response.json()

#     if response.status_code == 200:
#         weather_data = {
#             "city": city,
#             "temperature": data["main"]["temp"],
#             "weather": data["weather"][0]["description"],
#             "humidity": data["main"]["humidity"],
#             "wind_speed": data["wind"]["speed"]
#         }
#         return jsonify(weather_data)
#     else:
#         return jsonify({"error": "Failed to retrieve weather data"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
# import requests
# Url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f2687bb3ba514ebdb8a3b90a60c91a43"
# r=requests.get("url")
# print(r.text)



