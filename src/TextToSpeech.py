import pyttsx3

class TextToSpeech:
    def __init__(self):

      # initialize the text-to-speech module
      self.speech = pyttsx3.init()