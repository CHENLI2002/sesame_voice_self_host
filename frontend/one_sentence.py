import requests
from tools import play_sound

current_trial = "Hello World"
port = "8080"
ip = "http://80.225.232.52"
url = f"{ip}:{port}/generate_one_sentence"
query = {"text": current_trial}

response = requests.post(url, json=query)

if response.status_code == 200:
    print("We got a response!")

    with open("outputs/tmp.wav", "wb") as f:
        f.write(response.content)
        print("We got a file!")

else:
    print("Error: we got no response")

play_sound(path="outputs/tmp.wav")
