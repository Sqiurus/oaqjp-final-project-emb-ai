import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:

        formatted_response = response.json()['emotionPredictions'][0]['emotion']
        max_scored = max(formatted_response, key = formatted_response.get)
        formatted_response['dominant_emotion'] = max_scored

    elif response.status_code == 500:
        formatted_response = Noneformatted_response = None
        
    else:
        formatted_response = None

    return formatted_response