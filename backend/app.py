from flask import Flask, jsonify, request
from motion_detect import detect_threat
import os

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    video_name = data.get("video")

    if not video_name:
        return jsonify({"error": "Video name missing"}), 400

    video_path = os.path.join("..", "videos", video_name)

    if not os.path.exists(video_path):
        return jsonify({"error": "Video not found"}), 404

    threat = detect_threat(video_path)

    return jsonify({
        "camera": video_name,
        "threat": threat,
        "status": "Threat Detected" if threat else "Safe"
    })


if __name__ == "__main__":
    app.run(debug=True)
