"""
This module contains the Flask server for Emotion Detection.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route():
    """
    Endpoint to analyze the emotion of provided text.

    Args:
        None (uses request.args.get for 'textToAnalyze')

    Returns:
        JSON response with emotion analysis or error message
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get('error') == 'Invalid text! Please try again.':
        return jsonify({'error': 'Invalid text! Please try again.'}), 400

    if response['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again.'}), 400

    formatted_response = (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({'response': formatted_response}), 200


@app.route("/", methods=['GET'])
def render_index_page():
    """
    Renders the index.html template.

    Args:
        None

    Returns:
        HTML template rendered by Flask
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
