import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')

openai.api_base = os.getenv('API_BASE')

meta_prompt="Ты бот, который выполняет задачу по извлечению информации из текста. Твоя задача извлечь первое это карту получателя, второе это время операции и третье сумма перевода. В твоем ответе не доложно быть лишней информации и только то, что я назвал."

messages = []

def get_payments_info(prompt: str) -> str:
    messages.append({"role": "system", "content": meta_prompt})
    messages.append({"role": "user", "content": prompt})

    response_big = openai.ChatCompletion.create(
        model=os.getenv('MODEL'),
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=int(len(prompt) * 1.5),
    )

    response = response_big["choices"][0]["message"]
    return response['content'].encode('unicode-escape').decode('unicode-escape')