"""
nodes/retrieve.py
------------------
Graph node: Step 1 of the multi-step tool chain.

Responsibility: take the incoming question from graph state, call the
retriever tool, and write the retrieved chunks back into state for the
next node (`reason`) to consume.

Each node in this skeleton follows the same contract:
    def node_fn(state: dict) -> dict:
        ...
        return {**state, <new keys>}
This keeps nodes pure and testable in isolation (see tests/unit/).
"""

from agent.tools.retriever_tool import retrieve_documents


def retrieve_node(state: dict) -> dict:
    question = state["question"]
    chunks = retrieve_documents(question)
    return {**state, "retrieved_chunks": chunks}
