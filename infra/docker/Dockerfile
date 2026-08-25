# --------------------------------------------------------------------------
# Dockerfile for langgraph-rag-agent
#
# Why this lives under infra/docker/ instead of the repo root:
#   Keeps deployment/infra concerns visually and physically separated from
#   application source (src/). As we add more deployment patterns later
#   (static web, microservices, A2A) each will get its own infra/<pattern>/
#   subfolder without cluttering the repo root.
#
# Build from the REPO ROOT (not this folder) so the build context includes
# src/, requirements.txt, etc:
#   docker build -f infra/docker/Dockerfile -t langgraph-rag-agent:local .
# --------------------------------------------------------------------------

FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY src/ ./src/
COPY data/ ./data/

ENV PYTHONPATH=/app/src
ENV APP_ENV=container

# STUB entrypoint: runs the graph's __main__ block once for now.
# TODO (later session): replace with a real API server entrypoint
# (e.g. FastAPI + uvicorn) once we containerize as a service, not a script.
CMD ["python", "-m", "agent.graph"]
