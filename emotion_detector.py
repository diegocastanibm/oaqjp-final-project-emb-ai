import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # New format
    formatted_response = json.loads(response.text)
    dict_emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(dict_emotions, key=dict_emotions.get)
    dict_emotions["dominant_emotion"] = dominant_emotion

    return dict_emotions