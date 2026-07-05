from app.providers.llm.gemini import generate


class ContentService:
    async def generate(self, user_input: str) -> dict:
        text = await generate(user_input)

        return {
            "text": text,
            "platform": "telegram",
        }