from app.services.gemini import generate


async def generate_content(user_input: str) -> dict:
    text = await generate(user_input)

    return {
        "text": text,
        "platform": "telegram",
    }