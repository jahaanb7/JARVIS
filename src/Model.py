import os
from openrouter import OpenRouter

class Model:
  def __init__(self):
    self.api_key = os.getenv("OPENROUTER_API_KEY")

    #debug if the api_key returned null
    if not self.api_key:
      raise RuntimeError("not found") 

  def jarvis(self, text):
    client = OpenRouter(
      api_key = self.api_key,
        server_url="https://ai.hackclub.com/proxy/v1",
    )
    
    response = client.chat.send(
        model="google/gemini-3-flash-preview",
        messages=[{"role": "user", "content": text}],
        max_tokens=1024
    )
    
    answer = response.choices[0].message.content
    return answer
