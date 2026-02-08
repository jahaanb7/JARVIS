from src.Model import Model
from src.SpeechRecognition import SpeechRecognition
import textwrap
import time
from utils.TextFormat import TextFormat

class Main:
  def __init__(self):
    self.answerSpeed = 0.2

    #create instances for each class
    self.model = Model()
    self.speech = SpeechRecognition()
    self.formatter = TextFormat()

  def answer(self):
    #get question input from speech recognitiion
    question = self.speech.speech_to_text()

    #response
    text = self.model.jarvis(question)

    #format the text output for bullet, numbered lists, etc
    text = self.formatter.clean_markdown(text)

    paragraphs = text.split('\n\n')
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue

        #from stackoverflow found out that python has inbuilt text wrpper
        wrapper = textwrap.fill(paragraph, width=70)

        lines = wrapper.split('\n')
    
        for line in lines:
            words = line.split()

            for word in words:
                print(word, end=' ', flush=True)  #same line
                time.sleep(self.answerSpeed)  #delay in word by word
            print()
        print()

jarvis1 = Main()
jarvis1.answer()