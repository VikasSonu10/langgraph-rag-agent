"""
llm/client.py
-------------
Swappable LLM client. This is the ONLY place in the codebase that should
import a provider-specific SDK (openai, azure-openai, anthropic, etc).

Why this pattern:
    Across this curriculum we will swap frameworks (LangGraph -> Azure AI
    Foundry -> Bedrock -> Vertex) and clouds. Nodes/graph logic should never
    care which provider answers the prompt. They call `get_llm_client()`
    and depend only on the `.complete()` interface below.

STUB: no real provider call is wired up yet. Each branch raises
NotImplementedError with a clear TODO — implementation comes in a later
session once we start executing (not just scaffolding) the graph.
"""

from agent.config import settings


class LLMClient:
    def complete(self, prompt: str) -> str:
        raise NotImplementedError


class OpenAIClient(LLMClient):
    def complete(self, prompt: str) -> str:
        # TODO: wire up `openai` SDK using settings.llm_api_key / settings.llm_model
        raise NotImplementedError("OpenAIClient.complete not yet implemented")


class AzureOpenAIClient(LLMClient):
    def complete(self, prompt: str) -> str:
        # TODO: wire up `openai` SDK in Azure mode using settings.llm_api_base /
        # settings.llm_api_version / settings.llm_api_key
        raise NotImplementedError("AzureOpenAIClient.complete not yet implemented")


class AnthropicClient(LLMClient):
    def complete(self, prompt: str) -> str:
        # TODO: wire up `anthropic` SDK using settings.llm_api_key / settings.llm_model
        raise NotImplementedError("AnthropicClient.complete not yet implemented")


def get_llm_client() -> LLMClient:
    """Factory: returns the correct client based on LLM_PROVIDER env var."""
    provider = settings.llm_provider
    if provider == "azure_openai":
        return AzureOpenAIClient()
    if provider == "anthropic":
        return AnthropicClient()
    if provider == "openai":
        return OpenAIClient()
    raise ValueError(f"Unknown LLM_PROVIDER: {provider}")
