from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.services.conversation import extract_requirements
from app.services.guardrails import (
    is_offtopic,
    needs_clarification
)
from app.services.ranking import retrieve_assessments

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():
    return {"status": "ok"}



@app.post("/chat")
def chat(req: ChatRequest):

    messages = [m.dict() for m in req.messages]

    latest_user_message = messages[-1]["content"]

    if is_offtopic(latest_user_message):
        return {
            "reply": "I can only help with SHL assessments and catalog recommendations.",
            "recommendations": [],
            "end_of_conversation": False
        }

    state = extract_requirements(messages)

    if needs_clarification(state):

        if not state["skills"]:
            return {
                "reply": "What role or technical skills are you hiring for?",
                "recommendations": [],
                "end_of_conversation": False
            }

        if not state["seniority"]:
            return {
                "reply": "What seniority level are you hiring for?",
                "recommendations": [],
                "end_of_conversation": False
            }

    query = latest_user_message

    recommendations = retrieve_assessments(query)

    return {
        "reply": f"Here are {len(recommendations)} SHL assessments matching your requirements.",
        "recommendations": recommendations,
        "end_of_conversation": True
    }