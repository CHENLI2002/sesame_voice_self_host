import requests
from tools import play_sound

current_context_prev_conversation = "Bruh.... WTF"
url = "http://104.171.203.203:8080/generate_with_context"
query = {
    "previous_conversation": current_context_prev_conversation,
    "model": "gpt-3.5-turbo"
}

response = requests.post(url, json=query)

if response.status_code == 200:
    with open("outputs/tmp.wav", "wb") as f:
        f.write(response.content)
        print("Got response")
else:
    print("no response")

play_sound("outputs/tmp.wav")
