"""
graph.py
--------
LangGraph state graph wiring: defines the nodes and edges that make up
the multi-step RAG tool chain.

    retrieve_node -> reason_node -> answer_node

Why this file is separate from individual node files:
    `nodes/*.py` define WHAT each step does in isolation (unit-testable
    without any graph machinery). `graph.py` defines HOW they're wired
    together (the control flow / routing). This separation is what lets
    us later swap LangGraph for another orchestration framework (e.g.
    Azure AI Foundry's orchestration, or a hand-rolled state machine)
    without rewriting node logic — only this file changes.

STUB: the actual `langgraph` import and StateGraph construction is
commented out until we install dependencies and move from scaffold to
working code in the next session.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, END
from agent.nodes.retrieve import retrieve_node
from agent.nodes.reason import reason_node
from agent.nodes.answer import answer_node


class AgentState(TypedDict, total=False):
    question: str
    retrieved_chunks: list
    reasoning_decision: str
    final_answer: str


def build_graph():
    """Build and compile the LangGraph state graph for the RAG tool chain."""
    graph = StateGraph(AgentState)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("reason", reason_node)
    graph.add_node("answer", answer_node)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "reason")
    graph.add_edge("reason", "answer")
    graph.add_edge("answer", END)
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({"question": "What is this skeleton for?"})
    print(result["final_answer"])
