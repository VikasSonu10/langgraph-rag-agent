"""
nodes/answer.py
----------------
Graph node: Step 3 (final) of the multi-step tool chain.

Responsibility: synthesize the final answer from question + retrieved
context and write it to state as `final_answer`. This is the terminal
node the graph routes to once `reason_node` decides we're ready.

STUB: returns a templated placeholder instead of a real LLM completion.
"""


def answer_node(state: dict) -> dict:
    question = state["question"]
    chunks = state.get("retrieved_chunks", [])
    # TODO: replace with real LLM call: get_llm_client().complete(prompt)
    stub_answer = (
        f"[STUB ANSWER] Based on {len(chunks)} retrieved chunk(s), "
        f"here is a placeholder answer to: {question!r}"
    )
    return {**state, "final_answer": stub_answer}
