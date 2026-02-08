import sys
import os
from openrouter import OpenRouter

class JARVIS:
    def __init__(self):
        # load in environment variables from system (api_key(s))
        self.api_key = os.getenv("OPENROUTER_API_KEY")

        #debug if the api_key returned null
        if not self.api_key:
            raise RuntimeError("not found")
    
    def jarvis(self):
        client = OpenRouter(
          api_key = self.api_key,
            server_url="https://ai.hackclub.com/proxy/v1",
        )

        question = " ".join(sys.argv[1:]) 

        response = client.chat.send(
            model="google/gemini-3-flash-preview",
            messages=[
                {"role": "assistant", "content": question}
            ],
        )

        return response

    def answer(self):
        response = self.jarvis()
        answer = print(response.choices[0].message.content)
        return answer

jarvis1 = JARVIS()
jarvis1.answer()