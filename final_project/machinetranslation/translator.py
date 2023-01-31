import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text):
    """
        Function to translate English to French
    """
    if english_text != '':
        request = language_translator.translate(
                text=english_text,
                source='en',
                target='fr',)
        response_status = request.get_status_code()
        if response_status == 200:
            result = request.get_result()['translations'][0]['translation']
        else:
            result = "Error"
        french_text = result
    else:
        french_text = "Text is null"
    return french_text

def french_to_english(french_text):
    """
        Function to translate French to English
    """
    if french_text != '':
        request = language_translator.translate(
                text=french_text,
                source='fr',
                target='en',)
        response_status = request.get_status_code()
        if response_status == 200:
            result = request.get_result()['translations'][0]['translation']
        else:
            result = "Error"
        english_text = result
    else:
        english_text = "Text is null"
    return english_text
