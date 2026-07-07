from app.core.exceptions import GenerationError
from app.providers.llm.base import BaseLLMProvider
from app.schemas.content import ContentResponse


class ContentService:
    def __init__(self, provider: BaseLLMProvider) -> None:
        self.provider = provider

    async def generate(self, prompt: str, platform: str = "telegram") -> ContentResponse:
        try:
            text = await self.provider.generate(prompt)
            return ContentResponse(
                text=text,
                platform=platform,
                provider=self.provider.provider_name,
            )
        except Exception as exc:  # pragma: no cover - defensive guard
            raise GenerationError("Content generation failed") from exc

    async def stream(self, prompt: str):
        try:
            async for chunk in self.provider.stream(prompt):
                yield chunk
        except NotImplementedError:
            yield await self.provider.generate(prompt)
