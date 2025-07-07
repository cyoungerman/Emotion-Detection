from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)