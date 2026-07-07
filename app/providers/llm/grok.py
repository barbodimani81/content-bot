from app.core.config import get_settings
from app.providers.llm.base import BaseLLMProvider


class GrokProvider(BaseLLMProvider):
    provider_name = "grok"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        settings = get_settings()
        self.api_key = api_key or settings.grok_api_key
        self.model = model or settings.grok_model

    async def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Grok provider is scaffolded but not implemented yet"
        )
