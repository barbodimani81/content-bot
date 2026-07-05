from app.providers.llm.base import BaseLLMProvider


class ContentService:
    def __init__(
        self,
        provider: BaseLLMProvider,
    ) -> None:
        self.provider = provider

    async def generate(
        self,
        user_input: str,
    ) -> dict:
        text = await self.provider.generate(user_input)

        return {
            "text": text,
            "platform": "telegram",
        }