from app.core.config import get_settings
from app.core.exceptions import ProviderUnavailableError
from app.providers.llm.base import BaseLLMProvider
from app.providers.llm.gemini import GeminiProvider
from app.providers.llm.grok import GrokProvider


def build_llm_provider(name: str | None = None) -> BaseLLMProvider:
    settings = get_settings()
    provider_name = (name or settings.llm_provider).lower()

    if provider_name == "gemini":
        return GeminiProvider()

    if provider_name == "grok":
        return GrokProvider()

    raise ProviderUnavailableError(
        f"Unsupported LLM provider: {provider_name}"
    )
