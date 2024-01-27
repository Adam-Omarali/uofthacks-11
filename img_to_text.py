import base64
import requests
import os
import cohere
import time

openai_api_key = os.environ["OPENAI_API_KEY"]
cohere_api_key = os.environ["COHERE_API_KEY"]

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
def get_image_description(image_path):

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What's in this image?"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

def get_narraration(text):
    co = cohere.Client(cohere_api_key) # This is your trial API key
    response = co.generate(
    model='command',
    prompt=text + '\nMake a script in the tone of David attenborough regarding this image. The user wants to feel nostaligic. focus on quirky details. Just give me the story, no intro or closure.',
    max_tokens=500,
    temperature=1,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return ('Prediction: {}'.format(response.generations[0].text))

start = time.time()
desc = get_image_description("IMG_5562.JPG")
start2 = time.time()
print("openai image caption time", start2 - start)
narration = get_narraration(desc)
print("cohere image caption time", time.time() - start2)
print(narration)