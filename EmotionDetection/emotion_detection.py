import requests

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Text input is empty'
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 200:
        response_dict = response.json()
        emotion_predictions = response_dict['emotionPredictions'][0]['emotion']
        
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
        dominant_score = emotion_predictions[dominant_emotion]
        
        output = {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            'dominant_emotion': dominant_emotion.capitalize()
        }
        return output
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Bad request: Invalid input'
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Failed to get emotion predictions'
        }
