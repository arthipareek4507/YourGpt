from flask import Flask, request, jsonify, send_from_directory
import yourgpt
import os

app = Flask(__name__)

frontend_folder = os.path.join(os.path.dirname(__file__), "frontend")


# Display the website
@app.route("/")
def home():
    return send_from_directory(frontend_folder, "index.html")


# Load CSS and JavaScript files
@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(frontend_folder, filename)


# Receive messages and send chatbot responses
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    user_message = data.get("message", "")

    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({
            "response": "Please enter a valid message.",
            "should_exit": False
        }), 400

    cleaned_message = yourgpt.clean_text(user_message)

    response, should_exit = yourgpt.get_response(cleaned_message)

    return jsonify({
        "response": response,
        "should_exit": should_exit
    })

if __name__ == "__main__":
    app.run(debug=True)