"""Flask server for Emotion Detection application."""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def get_emotions():
    """
    Process the input text and return emotion analysis.
    Returns:
        dict: A dictionary containing emotion scores or an error message.
    """
    text = request.args.get("text")

    if not text:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "error": "Invalid text! Please try again!"
        }), 400

    result = emotion_detector(text)

    # Handle failed model result (dominant_emotion is None)
    if result.get("dominant_emotion") is None:
        result["error"] = "Invalid text! Please try again!"
        return jsonify(result), 400

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
