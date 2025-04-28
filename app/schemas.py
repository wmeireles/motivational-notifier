# app/schemas.py
from pydantic import BaseModel

class MessageCreate(BaseModel):
    text: str

class MessageOut(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
