# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Motivational Messages API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages/", response_model=schemas.MessageOut)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(text=message.text)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/messages/random", response_model=schemas.MessageOut)
def get_random_message(db: Session = Depends(get_db)):
    messages = db.query(models.Message).all()
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found.")
    return random.choice(messages)

@app.get("/messages/", response_model=list[schemas.MessageOut])
def get_all_messages(db: Session = Depends(get_db)):
    return db.query(models.Message).all()
