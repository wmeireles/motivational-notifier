from sqlalchemy import Column, Integer, String  # <-- ISSO ESTÁ FALTANDO
from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
