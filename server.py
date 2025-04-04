"""
Docstring: server.py
"""

# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from EmotionDetection.emotion_detector import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Docstring: sent_anal
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)


    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {response}. \
    The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """
    Docstring: render
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
