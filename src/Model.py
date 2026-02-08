import sys
import os
from utils import TextFormat
import time
import textwrap
from openrouter import OpenRouter

class Model:
  def __init__(self):
    self.api_key = os.getenv("OPENROUTER_API_KEY")

    #debug if the api_key returned null
    if not self.api_key:
      raise RuntimeError("not found") 
    
    self.ans_speed = 0.2

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

  def answer(self, question):
    text = self.jarvis(question)

    text = TextFormat.clean_markdown(text)

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
                time.sleep(self.ans_speed)  #delay in word by word
            print()
        print()

jarvis1 = Model()
jarvis1.answer()
