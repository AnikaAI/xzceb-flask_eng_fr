'''
translator
'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION2018='2018-05-01'

def englishToFrench(english_text):
    '''
    translates from english to french
    '''
    if english_text=="":
        french_text=""
    else:
        french_text = language_translator.translate(
        text=english_text,
        model_id="en-fr").get_result()['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    '''
    translates from french to english
    '''
    if french_text=="":
        english_text = ""
    else:
        english_text = language_translator.translate(
        text=french_text,
        model_id="fr-en").get_result()['translations'][0]['translation']
    return english_text

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION2018,
    authenticator=authenticator
)
