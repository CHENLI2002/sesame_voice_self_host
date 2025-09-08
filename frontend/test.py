import requests
import pyaudio
import wave

url = "http://104.171.203.203:8080/generate_one_sentence"
query = {"text": "Read me a sample sentence please!"}

response = requests.post(url, json=query)

if response.status_code == 200:
    print("We got a response!")

    with open("outputs/tmp.wav", "wb") as f:
        f.write(response.content)
        print("We got a file!")

else:
    print("Error: we got no response")

chunk = 1024
with wave.open("outputs/tmp.wav", "rb") as f:
    paudio = pyaudio.PyAudio()
    stream = paudio.open(format=paudio.get_format_from_width(f.getsampwidth()),
                         channels=f.getnchannels(),
                         rate=f.getframerate(),
                         output=True)
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    paudio.terminate()