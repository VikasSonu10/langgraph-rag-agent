"""
tools/retriever_tool.py
------------------------
Retrieval tool used by the `retrieve` node in the graph.

Why a "tools" package (separate from "nodes"):
    Nodes describe WHEN something happens in the graph (the control flow).
    Tools describe WHAT capability is being invoked (search, calculator,
    API call, DB query). Keeping tools separate lets the same tool be
    reused by multiple nodes/graphs, and lets us swap the retrieval
    implementation (in-memory -> vector DB -> Azure AI Search) without
    touching graph wiring.

STUB: returns hardcoded placeholder chunks. Real implementation (embedding
+ vector search over `data/docs`) comes once we move from scaffold to
working code.
"""

from agent.config import settings


def retrieve_documents(query: str, top_k: int = None) -> list[str]:
    """
    Retrieve the top_k most relevant document chunks for `query`.

    TODO: replace with real retrieval:
        1. Load/embed docs from settings.docs_path
        2. Similarity search against the query embedding
        3. Return top_k chunks with source metadata
    """
    k = top_k or settings.top_k
    # Placeholder stub output so downstream nodes have something to chain on.
    return [f"[STUB] Relevant chunk {i+1} for query: {query!r}" for i in range(k)]
