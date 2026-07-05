from app.providers.llm.base import BaseLLMProvider


class GrokProvider(BaseLLMProvider):
    async def generate(self, prompt: str) -> str:
        raise NotImplementedError