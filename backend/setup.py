import torch
from fastapi import FastAPI
from fastapi.responses import FileResponse
from transformers import CsmForConditionalGeneration, AutoProcessor
from reqs import oneSentenceReq
import io

model_dir = "../models/csm-1b"
device = "cuda" if torch.cuda.is_available() else "cpu"

app = FastAPI(version="1.0")

processor = AutoProcessor.from_pretrained(model_dir)
model = CsmForConditionalGeneration.from_pretrained(model_dir).to(device)

@app.post("/generate_one_sentence")
def tts(request: oneSentenceReq):
    input_text = "[0]" + request.text
    processed_input = processor(input_text, add_special_tokens=True).to(device)
    audio = model.generate(**processed_input, output_audio=True)
    processor.save_audio(audio, "../tmp/tmp.wav")
    return FileResponse("../tmp/tmp.wav", media_type="audio/wav", file_name="response.wav")