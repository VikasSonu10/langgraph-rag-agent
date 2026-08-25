"""
Unit test for retrieve_node in isolation (no graph, no LLM, no network).
This is the level of test we can run for every node using only the STUB
implementations — proves the wiring/contract is correct before any real
provider code is added.
"""

from agent.nodes.retrieve import retrieve_node


def test_retrieve_node_adds_chunks_to_state():
    state = {"question": "What is LangGraph?"}
    result = retrieve_node(state)

    assert "retrieved_chunks" in result
    assert isinstance(result["retrieved_chunks"], list)
    assert len(result["retrieved_chunks"]) > 0
    # original state keys must be preserved (nodes should never drop state)
    assert result["question"] == state["question"]
