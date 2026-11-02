"""Text -> vector conversion, used both when indexing documents and when searching.

The SAME model must be used for indexing and for querying, so the provider follows APP_MODE:

    local  -> text-embedding-3-small through the OpenAI API
    cloud  -> text-embedding-005 through Vertex AI (Google Cloud credentials)

Both produce 768-dimensional vectors. In cloud mode that number is fixed by the
Vector Search index (see .github/workflows/deploy.yml).

Existing local Chroma data must be re-indexed when switching embedding models.
"""
from functools import lru_cache

from langchain_google_vertexai import VertexAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from config.settings import settings
from exceptions import ConfigurationError


@lru_cache(maxsize=1)
def get_embeddings() -> OpenAIEmbeddings | VertexAIEmbeddings:
    if settings.is_cloud:
        if not settings.GCP_PROJECT:
            raise ConfigurationError("APP_MODE=cloud needs GCP_PROJECT_ID for Vertex AI embeddings.")
        return VertexAIEmbeddings(
            model=settings.embedding_model_name,
            project=settings.GCP_PROJECT,
            location=settings.GCP_REGION,
            dimensions=settings.embedding_dimensions,
        )

    if not settings.OPENAI_API_KEY:
        raise ConfigurationError("APP_MODE=local needs OPENAI_API_KEY in .env for embeddings.")
    return OpenAIEmbeddings(
        model=settings.local_embedding_model_name,
        api_key=settings.OPENAI_API_KEY,
        dimensions=settings.embedding_dimensions,
    )
