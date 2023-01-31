import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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



def englishToFrench(englishText):
    if englishText != '':
        request = language_translator.translate(
                text=englishText,
                source='en',
                target='fr',)
        response_status = request.get_status_code()
        if response_status == 200:
            result = request.get_result()['translations'][0]['translation']
        else:
            result = "Error"
        frenchText = result
    else:
        frenchText = "Text is null"
    return frenchText

def frenchToEnglish(frenchText):
    if frenchText != '':
        request = language_translator.translate(
                text=frenchText,
                source='fr',
                target='en',)
        response_status = request.get_status_code()
        if response_status == 200:
            result = request.get_result()['translations'][0]['translation']
        else:
            result = "Error"
        englishText = result
    else:
        englishText = "Text is null"
    return englishText