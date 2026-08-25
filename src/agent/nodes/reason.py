"""
nodes/reason.py
----------------
Graph node: Step 2 of the multi-step tool chain.

Responsibility: given the retrieved chunks + original question, decide
whether more tool calls are needed or whether we have enough context to
answer. This is where a "multi-step tool chain" earns its name — in the
full implementation this node may loop back to `retrieve` (e.g. broaden
the search) before handing off to `answer`.

STUB: always proceeds straight to answer; no real reasoning/looping wired
up yet.
"""

from agent.llm.client import get_llm_client


def reason_node(state: dict) -> dict:
    llm = get_llm_client()
    # TODO: prompt the LLM with question + retrieved_chunks, decide:
    #   - "need_more_context" -> route back to retrieve_node
    #   - "ready" -> route to answer_node
    # For now, always mark ready (single-pass RAG).
    return {**state, "reasoning_decision": "ready", "_llm_client_ref": llm.__class__.__name__}
