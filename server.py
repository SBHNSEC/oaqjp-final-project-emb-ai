"""
Flask server used as backend server to NLP - Emotion Detection.
This server appliaction uses the Watson NLP Library to score 
the emotions in the statement and finally reveal the dominant 
emotion among all the scored emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the Homepage of the NLP - Emotion Detection Application"""
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Detects the Emotions of the User Input Statement"""
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}"
        f"'disgust': {result['disgust']}"
        f"'fear': {result['fear']}"
        f"'joy': {result['joy']}"
        f"'sadness': {result['sadness']}"
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
