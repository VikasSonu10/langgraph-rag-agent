# langgraph-rag-agent

**Status: Skeleton / Session 1 of the hands-on AI deployment curriculum.**
This is a *base skeleton*, not a complete project — every node/tool/config
file contains real structure and comments but STUB logic (no live LLM
calls yet). Implementation is filled in progressively in later sessions.

## What this agent will eventually do

A **RAG-style single agent** with a **multi-step tool chain**:

```
retrieve  →  reason  →  answer
```

1. `retrieve` — pull relevant chunks from a small local doc set
2. `reason` — decide if there's enough context, or loop back for more
3. `answer` — synthesize the final response

Orchestrated with **LangGraph**. The LLM backend is **swappable via env
var** (`LLM_PROVIDER`) so the same graph logic can run against OpenAI,
Azure OpenAI, or Anthropic without code changes — this matters because
later sessions in the curriculum swap frameworks and clouds, and we don't
want agent logic rewritten every time.

## Why this folder structure (and not a flat script)

This mirrors a real production repo layout, scaled down. Each top-level
folder maps to a distinct *concern*, so as the project grows (multi-agent,
new deployment patterns, new clouds) things land in an obvious place
instead of one giant file.

```
langgraph-rag-agent/
├── src/agent/              # Application code — the only folder that ships in the container
│   ├── graph.py             # HOW nodes are wired together (control flow / orchestration)
│   ├── nodes/                # WHAT each graph step does, in isolation
│   │   ├── retrieve.py       #   step 1: fetch context
│   │   ├── reason.py         #   step 2: decide next action
│   │   └── answer.py         #   step 3: synthesize final answer
│   ├── tools/                # Reusable capabilities nodes call (search, calculators, APIs)
│   │   └── retriever_tool.py
│   ├── llm/                  # The ONLY place that imports a provider SDK
│   │   └── client.py         #   swappable LLM client, selected via config
│   └── config.py             # All env-driven settings — single source of truth
│
├── data/docs/                # Sample documents for the retrieval step to index
│
├── tests/
│   ├── unit/                 # Test each node in isolation — no graph, no network
│   └── integration/          # Test the full retrieve→reason→answer chain together
│
├── infra/                    # Deployment/infra concerns, kept OUT of application code
│   ├── docker/Dockerfile     #   containerization (Phase 1 deployment target)
│   └── azure/*.bicep         #   IaC stub for Azure Container Apps
│
├── .github/workflows/ci.yml  # CI stub: install → lint → test on every push/PR
│
├── docs/adr/                 # Architecture Decision Records — the "why", not just "what"
│
├── .env.example               # Documents every required env var without leaking secrets
├── requirements.txt           # Python dependencies (minimal for now — scaffold session)
├── pyproject.toml             # Project metadata + pytest config
└── .gitignore
```

### Why the separation matters (the enterprise reasoning)

| Folder | Purpose | What breaks if you skip this separation |
|---|---|---|
| `nodes/` vs `graph.py` | nodes = *what*, graph = *how* they connect | Swapping LangGraph for another orchestrator later means rewriting business logic, not just wiring |
| `tools/` | reusable capabilities, independent of any one node | Duplicated retrieval/search code across nodes |
| `llm/client.py` | the *only* file that imports a provider SDK | Provider-specific code leaks into business logic; swapping providers becomes a repo-wide find/replace |
| `config.py` | every env-driven setting, one file | Hardcoded values scattered across files; can't promote the same code from local → dev → prod without edits |
| `infra/` separate from `src/` | deployment concerns never mixed into app code | Container image accidentally ships IaC files; infra changes trigger unnecessary app rebuilds |
| `tests/unit` vs `tests/integration` | isolate a single node vs. the whole chain | Slow test suite (everything requires full graph execution); hard to pinpoint which step broke |
| `docs/adr/` | recorded rationale for decisions | Future sessions (or teammates) can't tell if a design choice was deliberate |

## Running the stub locally

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m agent.graph
```

## Running tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Building the container (once we reach the deploy step)

```bash
docker build -f infra/docker/Dockerfile -t langgraph-rag-agent:local .
docker run --env-file .env langgraph-rag-agent:local
```

## Curriculum context

This is **Phase 1** of a multi-phase hands-on curriculum: Azure first
(free-tier account + Container Apps), then the same skeleton pattern gets
repeated across AWS (Bedrock), GCP (Vertex), and a free-tier alternative
cloud — followed by multi-agent, microservices, A2A, load testing,
approval gates, and cluster autoscaling exercises.

## Next session

- Fill in real dependencies (`langgraph`, an LLM SDK) in `requirements.txt`
- Wire up `graph.py`'s real `StateGraph` (currently a plain-Python stand-in)
- Implement real retrieval in `retriever_tool.py`
- `git init`, first commit, push to a remote (Git / Azure DevOps)
