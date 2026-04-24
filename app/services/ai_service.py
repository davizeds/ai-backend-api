from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)



def generate_response(text: str):
    response=client.chat.completions.create(model='gpt-4.1-mini',messages=[{'role': "user",'content': text}])
    resposta=response.choices[0].message.content
    return resposta
