"""This module detects emotions for text inputs"""
import json
import requests

def emotion_detector(text_to_analyze):
    """This function returns emotions for input text"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header_json = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = header_json)
    response_json = json.loads(response.text)
    anger = response_json['emotionPredictions'][0]['emotion']['anger']
    disgust = response_json['emotionPredictions'][0]['emotion']['disgust']
    fear = response_json['emotionPredictions'][0]['emotion']['fear']
    joy = response_json['emotionPredictions'][0]['emotion']['joy']
    sadness = response_json['emotionPredictions'][0]['emotion']['sadness']
    scores = {'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness}
    dominant_emotion = max(scores, key=scores.get)
    return {'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness,
    'dominant_emotion': dominant_emotion}
