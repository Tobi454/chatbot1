from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Simple rule-based chatbot responses
responses = {
    "hi": "Hello! How are you doing?",
    "hello": "Hi there! 😊",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Come chat again soon!",
    "default": "Sorry, I don’t understand that yet. 😅"
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

@app.route("/")
def home():
    # Serve index.html from same folder as app.py
    return send_from_directory(os.getcwd(), "index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["message"]
    response = get_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
