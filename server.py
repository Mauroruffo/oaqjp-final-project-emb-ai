"""Routes with backend communication"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_emotion():
    """Receive emotion from html"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return ("For the given statement, the system response is 'anger': " + str(anger)
    + ", 'disgust': " + str(disgust)
    + ", 'fear': " + str(fear)
    + ", 'joy': " + str(joy)
    + " and 'sadness': " + str(sadness)
    + ". The dominant emotion is " + str(dominant_emotion) + ".")

@app.route('/')
def render_index_page():
    """Render html template"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
