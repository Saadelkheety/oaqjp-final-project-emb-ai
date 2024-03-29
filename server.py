from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detectection():
    text_to_analyse = request.args.get('text_to_analyse')
    if text_to_analyse is None:
        return ('No text to analyse', 400)
    emotion = emotion_detector(text_to_analyse)
    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {emotion}"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)