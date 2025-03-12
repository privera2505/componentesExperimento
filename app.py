from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def receive_message():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400
    
    message = data["message"]
    print("Received message:", message)
    return jsonify({"success": True, "received": message})