from google import genai

from app.core.config import settings
from app.providers.llm.base import BaseLLMProvider

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class GeminiProvider(BaseLLMProvider):
    async def generate(self, prompt: str) -> str:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text