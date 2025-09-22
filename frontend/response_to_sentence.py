import requests
from tools import play_sound

current_context_prev_conversation = "I just moved to a new city last week, and everything feels so overwhelming. The streets are crowded, I don’t know anyone here, and I’m not sure where to even start making friends. Sometimes I feel excited, but other times I just feel lost."
port = "8080"
ip = "http://80.225.232.52"
url = f"{ip}:{port}/generate_with_context"
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
