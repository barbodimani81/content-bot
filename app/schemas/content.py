from dataclasses import dataclass


@dataclass(slots=True)
class ContentRequest:
    user_prompt: str
    platform: str = "telegram"
    language: str = "en"
    tone: str = "professional"
    content_type: str = "text"