import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }

    final_output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)
    except requests.exceptions.RequestException:
        return final_output

    if response.status_code == 400:
        return final_output
    
    if response.status_code != 200:
        return final_output

    try:
        response_dict = json.loads(response.text)
        prediction = response_dict.get("emotionPredictions",[])

        if not prediction:
            return final_output
        
        else:
            emotions = prediction[0].get("emotion",{})
            
            final_output["anger"]= float(emotions.get('anger', 0))
            final_output["disgust"]= float(emotions.get('disgust', 0))
            final_output["fear"]= float(emotions.get('fear', 0))
            final_output["joy"]= float(emotions.get('joy', 0))
            final_output["sadness"]= float(emotions.get('sadness', 0))

            emotionDominantDict= {
                "anger": final_output["anger"],
                "disgust": final_output["disgust"],
                "fear": final_output["fear"],
                "joy": final_output["joy"],
                "sadness": final_output["sadness"]
            }

            if not any(emotionDominantDict.values()):
                final_output["dominant_emotion"] = ''
            else:
                final_output["dominant_emotion"] = max(emotionDominantDict, key=emotionDominantDict.get)
    
    except (KeyError, ValueError, json.JSONDecodeError):
        return final_output
        
    return final_output