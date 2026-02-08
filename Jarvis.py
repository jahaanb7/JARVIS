import sys
import os
import pyttsx3
import speech_recognition as sr
from openrouter import OpenRouter

class JARVIS:
    def __init__(self):
        # load in environment variables from system (api_key(s))
        self.api_key = os.getenv("OPENROUTER_API_KEY")

        # initialize the text-to-speech module
        self.speech = pyttsx3.init()

        #initialize the speech-to-text module
        self.recognizer = sr.Recognizer()

        #debug if the api_key returned null
        if not self.api_key:
            raise RuntimeError("not found")
        
    
        
    def speech_to_text(self):
        with sr.Microphone() as microphone:
            audio = self.recognizer.adjust_for_ambient_noise(microphone)
            audio = self.recognizer.listen(microphone, 5, 30)

        text = self.recognizer.recognize_google(audio)

        print(f"... {text}")

        return text

    
    def jarvis(self, text):
        client = OpenRouter(
          api_key = self.api_key,
            server_url="https://ai.hackclub.com/proxy/v1",
        )

        response = client.chat.send(
            model="google/gemini-3-flash-preview",
            messages=[
                {"role": "assistant", "content": text}
            ],
        )
        
        answer = print(response.choices[0].message.content)

        return answer

    def answer(self):
        question = self.speech_to_text()

        answer = self.jarvis(question)
        print(f"Jarvis: {answer}")

jarvis1 = JARVIS()
jarvis1.answer()