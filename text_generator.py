import openai
import re
from api_key import API_KEY
openai.api_key=API_KEY
model_engine="gpt-3.5-turbo-instruct"
text=input("What topic you want to write about: ")
prompt=text
print("The AI BOT is trying to generate a new text for you")
completions=openai.Completion.create(
  engine=model_engine,
  prompt="Give me a few paragraphs on the topic: "+prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)
generated_text=completions.choices[0].text
with open("generated_text.txt","w") as file:
  file.write(generated_text.strip())
print("The text has been generated successfully!!") 
