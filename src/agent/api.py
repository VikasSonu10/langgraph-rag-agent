from fastapi import FastAPI
from pydantic import BaseModel

from agent.graph import build_graph


class QuestionRequest(BaseModel):
    question: str


app = FastAPI(title="LangGraph RAG Agent API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(payload: QuestionRequest):
    graph = build_graph()
    result = graph.invoke({"question": payload.question})
    return {"answer": result["final_answer"]}
