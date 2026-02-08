import sys
import os
import pyttsx3
import speech_recognition as sr
import time
import textwrap
import re
from openrouter import OpenRouter

class JARVIS:
    def __init__(self):
        # load in environment variables from system (api_key(s))
        self.api_key = os.getenv("OPENROUTER_API_KEY")

        # initialize the text-to-speech module
        self.speech = pyttsx3.init()

        #initialize the speech-to-text module
        self.recognizer = sr.Recognizer()



    
    

    
    