import wave

import pyaudio


def play_sound(path: str):
    chunk = 1024
    with wave.open(path, "rb") as f:
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