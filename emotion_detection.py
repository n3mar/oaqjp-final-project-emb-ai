"""This module detects emotions for text inputs"""
import requests

def emotion_detector(text_to_analyze):
    """This function returns emotions for input text"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header_json = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = header_json)
    return response.text
    