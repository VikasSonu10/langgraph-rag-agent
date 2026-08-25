"""
config.py
---------
Centralized, env-driven configuration for the agent.

Why this exists (enterprise pattern):
    Hardcoding provider names, model names, or credentials inside node/tool
    code makes the skeleton impossible to port across frameworks (LangGraph
    today, Azure AI Foundry / Bedrock / Vertex tomorrow) or across clouds.
    Every setting that could change between environments (local, dev, stage,
    prod) or between cloud providers lives here and ONLY here.

Usage:
    from agent.config import settings
    settings.llm_provider  # "azure_openai" | "openai" | "anthropic" | ...
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    # --- LLM backend (swappable) ---
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")  # azure_openai | openai | anthropic
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_api_base: str = os.getenv("LLM_API_BASE", "")  # required for azure_openai
    llm_api_version: str = os.getenv("LLM_API_VERSION", "")  # required for azure_openai

    # --- Retrieval ---
    docs_path: str = os.getenv("DOCS_PATH", "data/docs")
    top_k: int = int(os.getenv("RETRIEVAL_TOP_K", "3"))

    # --- Runtime ---
    environment: str = os.getenv("APP_ENV", "local")  # local | dev | staging | prod
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
