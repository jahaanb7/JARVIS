import sys
import os
import speech_recognition as sr

class SpeechRecognition:
  def __init__(self):
    self.recognizer = sr.Recognizer()

    #adjustable variables
    self.timeLimit = 100
    self.phraseLimit = 7

  def speech_to_text(self):

    # allow the file and module to access the microphone
    # source for the conversion
    with sr.Microphone() as microphone:

        #remove background noise
        audio = self.recognizer.adjust_for_ambient_noise(microphone)

        #listen for 30 secs and dont reply if nothing is said in 5 sec
        audio = self.recognizer.listen(microphone, self.phraseLimit, self.timeLimit)

    text = self.recognizer.recognize_google(audio)

    try:
      print(f"You said:{text}")
      return text
    
    except sr.UnknownValueError:
      raise RuntimeError("Could not understand audio")

    except sr.RequestError as error:
        raise RuntimeError("Service isnt working; {0}".format(error))