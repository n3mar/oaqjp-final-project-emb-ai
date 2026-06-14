from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    output = (f"For the given statement, the system response is 'anger': {res['anger']}, "
    f"'disgust': {res['disgust']}, 'fear': {res['fear']}, "
    f"'joy': {res['joy']} and 'sadness': {res['sadness']}. "
    f"The dominant emotion is {res['dominant_emotion']}.")
    return output

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
