import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

from memory import memory

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "CaineAI is running!"}

@app.post("/chat")
def chat(request: ChatRequest):

    memory.add_user(request.message)

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=memory.history()
    )

    reply = response.choices[0].message.content

    memory.add_ai(reply)

    return {
        "reply": reply
    }
