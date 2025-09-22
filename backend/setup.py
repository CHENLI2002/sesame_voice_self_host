import torch
from fastapi import FastAPI
from fastapi.responses import FileResponse
from transformers import CsmForConditionalGeneration, AutoProcessor
from reqs import oneSentenceReq, generatePrevContextReq
import io
import os

from langchain.chat_models import init_chat_model


model_dir = "sesame/csm-1b"
device = "cuda" if torch.cuda.is_available() else "cpu"

app = FastAPI(version="1.0")

processor = AutoProcessor.from_pretrained(model_dir)
model = CsmForConditionalGeneration.from_pretrained(model_dir).to(device)

@app.post("/generate_one_sentence")
def generate_one_sentence(request: oneSentenceReq):
    input_text = "[0]" + request.text
    return _return_file(input_text)

def _return_file(input_text):
    p_input = processor(input_text, add_special_tokens=True).to(device)
    audio = model.generate(**p_input, output_audio=True)
    processor.save_audio(audio, "../tmp/tmp.wav")
    return FileResponse("../tmp/tmp.wav", media_type="audio/wav", filename="response.wav")

def _infer_next_sentence(text: str, model_name: str):
    chat_model = init_chat_model(model_name, model_provider="openai")
    result = chat_model.invoke("Respond a sentence to: " + text)
    return result.content

@app.post("/generate_with_context")
def generate_with_context(request: generatePrevContextReq):
    previous_context = request.previous_conversation
    next_sentence = _infer_next_sentence(previous_context, "gpt-3.5-turbo")
    return _return_file("[0]" + next_sentence)
