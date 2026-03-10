#!/usr/bin/env python3
"""
Market Research Assistant - Web API
FastAPI wrapper to expose the agent as an HTTP service.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from agent import MarketResearchAgent

app = FastAPI(title="Market Research Agent")
agent = MarketResearchAgent()


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    question: str
    answer: str


@app.get("/")
def root():
    return {"status": "ok", "message": "Market Research Agent is running"}


@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    answer = agent.ask(request.question)
    return AnswerResponse(question=request.question, answer=answer)


@app.post("/clear")
def clear():
    agent.clear_history()
    return {"status": "ok", "message": "Conversation history cleared"}
