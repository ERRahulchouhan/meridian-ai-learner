"""The OpenAI chat model used by both the RAG chain and the agents."""
from functools import lru_cache

from langchain_openai import ChatOpenAI

from config.settings import settings
from exceptions import ConfigurationError


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    """Create the chat model on first use (not at import time) and reuse it afterwards."""
    if not settings.OPENAI_API_KEY:
        raise ConfigurationError("OPENAI_API_KEY is empty. Add your OpenAI API key to .env.")
    return ChatOpenAI(
        model=settings.llm_model_name,
        api_key=settings.OPENAI_API_KEY,
        temperature=settings.llm_temperature,
    )


def extract_text(content) -> str:
    """Join text blocks when a model returns structured content."""
    if isinstance(content, list):
        return "\n".join(
            block.get("text", "") for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return content
