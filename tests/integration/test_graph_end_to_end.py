"""
Integration test: runs the full retrieve -> reason -> answer chain
end-to-end through build_graph(), rather than testing nodes in isolation.
Still uses STUB node implementations (no real LLM/network calls), so this
is safe to run in CI without API keys until real providers are wired up.
"""

from agent.graph import build_graph


def test_full_chain_produces_final_answer():
    app = build_graph()
    result = app.invoke({"question": "What is this skeleton for?"})

    assert "final_answer" in result
    assert "retrieved_chunks" in result
    assert result["reasoning_decision"] == "ready"
