import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

from prompt import SYSTEM_PROMPT

# ----------------------------
# OpenAI Client
# ----------------------------

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ----------------------------
# FastAPI App
# ----------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Memory
# ----------------------------

conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

# ----------------------------
# Request Model
# ----------------------------

class ChatRequest(BaseModel):
    message: str

# ----------------------------
# Chat Endpoint
# ----------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    conversation_history.append({
        "role": "user",
        "content": request.message
    })

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=conversation_history
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return {
        "reply": reply
    }

# ----------------------------
# Health Check
# ----------------------------

@app.get("/")
def home():
    return {
        "status": "CaineAI is running!"
    }
