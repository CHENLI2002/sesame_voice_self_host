from pydantic import BaseModel

class oneSentenceReq(BaseModel):
    text: str

class generatePrevContextReq(BaseModel):
    previous_conversation: str
    model: str
