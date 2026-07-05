from app.providers.llm.gemini import GeminiProvider
from app.services.content import ContentService


class ContentOrchestrator:
    def __init__(self) -> None:
        provider = GeminiProvider()

        self.content_service = ContentService(
            provider=provider,
        )

    async def generate(
        self,
        user_input: str,
    ) -> dict:
        return await self.content_service.generate(
            user_input,
        )