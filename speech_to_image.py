from monsterapi import client
import requests
import webbrowser

import speech_recognition as sr

recognizer = sr.Recognizer()

# MonsterAPI key
api_key ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjIxYzBmMTg2MDQzMGMxNzNmMjdkYjVjODUxZjk0MGY2IiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDhUMTM6MTA6MzEuOTk3MjkyIn0.JBo9k_xXBEW-fTHHm1v4b7KXIQz2OqlJVS1S9RDp3wg'
# Initialize client
monster_client = client(api_key)


# Prompt
prompt = with sr.Microphone() as source:
 print("Speak something...")
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    text = recognizer.recognize_google(audio, language='en-US')
    print("You said: ", text)

# Model
model = 'txt2img'

# Input data
input_data = {
    'prompt': f'{prompt}',
    'negprompt': 'bad anatomy',
    'samples': 1,
    'steps': 50,
    'aspect_ratio': 'square',
    'guidance_scale': 7.5,
    'seed': 2414,
}

result = monster_client.generate(model, input_data)

img_url = result['output'][0]

file_name = "generated_image.jpg"

# Download the image
response = requests.get(img_url)

if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print("Image downloaded")

    # Open the image
    webbrowser.open(file_name)

else:
    print("Failed to download")    