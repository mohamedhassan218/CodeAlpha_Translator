"""
    Module handles the process of calling the Azure API with the text and 
    get the translated one. 
    
    @author  Mohamed Hassan
    @since   2024-5-2
"""
import requests, uuid, json
from dotenv import load_dotenv
import os

# Load environment variables.
load_dotenv()
key = os.environ["KEY_ENDPOINT"]
endpoint = "https://api.cognitive.microsofttranslator.com"
location = os.environ["RESOURCE_LOCATION"]

def translate(text, from_language, to_language):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': from_language,
        'to': to_language
    }
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response

if __name__ == '__main__':
    response = translate('Hello', 'en', 'ar')
    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))