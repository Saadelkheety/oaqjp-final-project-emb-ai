import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json=input_data, headers=headers).json()
    emotion = res['emotionPredictions'][0]['emotion']
    emotion_to_return = {
        'anger': emotion.get('anger'),
        'disgust': emotion.get('disgust'),
        'fear': emotion.get('fear'),
        'joy': emotion.get('joy'),
        'sadness': emotion.get('sadness')
    }
    emotion_to_return['dominant_emotion'] = max(emotion, key=emotion.get)
    return emotion_to_return