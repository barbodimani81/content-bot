from app.providers.llm.base import BaseLLMProvider


class ContentService:
    def __init__(
        self,
        provider: BaseLLMProvider,
    ) -> None:
        self.provider = provider

    async def generate(
        self,
        prompt: str,
    ) -> dict:
        text = await self.provider.generate(prompt)

        return {
            "text": text,
            "platform": "telegram",
        }