from pydantic import BaseModel

class oneSentenceReq(BaseModel):
    text: str
