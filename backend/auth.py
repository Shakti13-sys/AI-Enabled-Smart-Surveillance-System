from flask import request, jsonify

API_KEY = "ADMIN-1234"

def require_auth():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
