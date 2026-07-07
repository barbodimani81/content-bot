from app.core.config import get_settings
from app.core.exceptions import ProviderUnavailableError
from app.providers.llm.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):
    provider_name = "gemini"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        settings = get_settings()
        self.api_key = api_key or settings.gemini_api_key
        self.model = model or settings.gemini_model
        self._client = None

    def _client_or_raise(self):
        if not self.api_key:
            raise ProviderUnavailableError("Gemini API key is not configured")

        if self._client is None:
            try:
                from google import genai
            except ImportError as exc:  # pragma: no cover - optional dependency
                raise ProviderUnavailableError(
                    "google-genai is not installed"
                ) from exc

            self._client = genai.Client(api_key=self.api_key)

        return self._client

    async def generate(self, prompt: str) -> str:
        client = self._client_or_raise()
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text or ""
