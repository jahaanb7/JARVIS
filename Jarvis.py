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

        #adjustable variables
        self.timeLimit = 1000
        self.phraseLimit = 10
        self.ans_speed = 0.2

        self.start_ans = ""

        #debug if the api_key returned null
        if not self.api_key:
            raise RuntimeError("not found")     
        
    def clean_markdown(self, text):

        # This part was done with Claude

        # Remove bold/italic markers
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)  # bold+italic
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)      # bold
        text = re.sub(r'\*(.+?)\*', r'\1', text)          # italic
        text = re.sub(r'__(.+?)__', r'\1', text)          # bold alt
        text = re.sub(r'_(.+?)_', r'\1', text)            # italic alt

        # Convert headers to emphasized text
        text = re.sub(r'^### (.+)$', r'\n\1:', text, flags=re.MULTILINE)
        text = re.sub(r'^## (.+)$', r'\n\1:', text, flags=re.MULTILINE)
        text = re.sub(r'^# (.+)$', r'\n\1:', text, flags=re.MULTILINE)

        # Convert list items
        text = re.sub(r'^\* ', r'  • ', text, flags=re.MULTILINE)
        text = re.sub(r'^\- ', r'  • ', text, flags=re.MULTILINE)

        # Clean up horizontal rules
        text = re.sub(r'^---+$', r'', text, flags=re.MULTILINE)

        # Remove extra blank lines (more than 2 in a row)
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()
        
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
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Service isnt working; {0}".format(e))

    
    def jarvis(self, text):
        client = OpenRouter(
          api_key = self.api_key,
            server_url="https://ai.hackclub.com/proxy/v1",
        )

        response = client.chat.send(
            model="google/gemini-3-flash-preview",
            messages=[
                {"role": "user", "content": text}
            ],
        )
        
        answer = response.choices[0].message.content

        return answer

    def answer(self):
        question = self.speech_to_text()
        text = self.jarvis(question)

        text = self.clean_markdown(text)

        paragraphs = text.split('\n\n')
        for paragraph in paragraphs:
            if not paragraph.strip():
                continue

            #from stackoverflow found out that python has inbuilt text wrpper
            wrapper = textwrap.fill(paragraph, width=70)
            words = wrapper.split()

            for word in words:
                print(word, end=' ', flush=True)  #same line
                time.sleep(self.ans_speed)  #delay in word by word
            print()

    def run(self):
        self.answer()


jarvis = JARVIS()
jarvis.run()