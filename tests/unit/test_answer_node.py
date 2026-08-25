from agent.nodes.answer import answer_node


def test_answer_node_produces_final_answer():
    state = {"question": "What is LangGraph?", "retrieved_chunks": ["chunk 1", "chunk 2"]}
    result = answer_node(state)

    assert "final_answer" in result
    assert isinstance(result["final_answer"], str)
    assert len(result["final_answer"]) > 0
