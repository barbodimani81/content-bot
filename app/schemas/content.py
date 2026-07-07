from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True)
class ContentRequest:
    user_prompt: str
    platform: str = "telegram"
    language: str = "en"
    tone: str = "professional"
    content_type: str = "text"
    user_id: int | None = None


@dataclass(slots=True)
class ContentResponse:
    text: str
    platform: str = "telegram"
    provider: str = "unknown"
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


@dataclass(slots=True)
class ConversationMessage:
    role: str
    content: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
