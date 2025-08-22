from EmotionDetection import emotion_detector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    textToAnalyze = request.args.get("textToAnalyze")
    result = emotion_detector(textToAnalyze)

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