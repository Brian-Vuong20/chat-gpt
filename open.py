import os
from dotenv import *
import openai

load_dotenv(find_dotenv("key.env"))

openai.api_key = os.getenv("OPEN_AI_API")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "Reponse with how are you"},
              {"role": "system", "content": "Reponse with asking any plan for today"},
              {"role": "system",
                  "content": "Reponse with telling dad joke if asked tell me story"},

              {"role": "user", "content": "Can you tell story"},
              ]
)
# print(completion)
print(completion)
