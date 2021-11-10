import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
def englishToFrench(englishText):
    #hello
    #goodbye
    #goodday
    #goodnight
    return frenchText 
    def frenchToEnglish(frenchText):
    #bonjour
    #aurevoir
    #bonnejournee
    #bonsoir
    return englishText 