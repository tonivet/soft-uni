import requests 
import json 


# Choose ollama server
url = "http://localhost:11434"

while True:
    try: 
        r = requests.get(url) 
        if r.status_code == 200:
            break
    except requests.exceptions.ConnectionError as conerr: 
        print("localhost is not active.")
        url = "http://" + input("Please enter ollama server address and port!\n http://")


# Retrieving available models from ollama list
MODEL = ""

headers = {
    "Content-Type": "application/json"
}

URL = url + '/api/tags'

response = requests.get(URL, headers=headers)
models = response.json()
models_list = [model["name"] for model in models['models']]

while True:
    print(f"Choose а model!")
    x = 1
    for model in models_list:
        print(f"{x}) {model}")
        x +=1

    selected_model = input()

    if selected_model.isnumeric() and int(selected_model) <= len(models_list):
            break

MODEL = models_list[int(selected_model) - 1]


# Start conversation
print("AI : Welcome to chat! To quit the chat type 'quit', 'exit' or 'close'!")

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

    URL = url + '/api/generate'

    response = requests.post(URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        answer = response.text
        data = json.loads(answer)
        actual_answer = data["response"]
        print("AI :", actual_answer)
    else:
        print("Error: ", response.status_code, response.text )
        quit()