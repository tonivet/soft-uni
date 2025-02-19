import requests 
import json 

print("AI : Welcome to chat! Type 'quit', 'exit' or 'close' to exit the chat!")


# Find ollama server
url = input("Please write ollama address like 'http://loclalhost'.\n http://")

URL = f"http://{url}:11434"


# Retrieving available models from ollama list
MODEL = ""

headers = {
    "Content-Type": "application/json"
}

url = URL + '/api/tags'

response = requests.get(url, headers=headers)
models = response.json()
models_list = [model["name"] for model in models['models']]

print(f"Choose model!")
x = 1
for model in models_list:
    print(f"{x}) {model}")
    x +=1

sleeted_model = int(input())

MODEL = models_list[sleeted_model - 1]


# Start conversation
print(f"AI: Ask me something!")

while True:

    question = input("User: ")

    if question.lower() in ['close', 'exit', 'quit']:
        print("Have a nice day!")
        quit()

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "prompt": question,
        "stream": False
    }

    url = URL + '/api/generate'

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        answer = response.text
        data = json.loads(answer)
        actual_answer = data["response"]
        print("AI :", actual_answer)
    else:
        print("Error: ", response.status_code, response.text )
        quit()