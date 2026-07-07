from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.core.exceptions import PromptBuildError
from app.schemas.content import ContentRequest, ConversationMessage


class BasePromptBuilder(ABC):
    @abstractmethod
    def build(
        self,
        request: ContentRequest,
        history: Sequence[ConversationMessage] | None = None,
    ) -> str:
        """Build a complete prompt for the provider."""


class TelegramPromptBuilder(BasePromptBuilder):
    system_prompt = "You are an expert AI content creator."

    def build(
        self,
        request: ContentRequest,
        history: Sequence[ConversationMessage] | None = None,
    ) -> str:
        try:
            parts = [
                self.system_prompt,
                "",
                f"Platform: {request.platform}",
                f"Language: {request.language}",
                f"Tone: {request.tone}",
                f"Content Type: {request.content_type}",
            ]

            if history:
                parts.extend(
                    [
                        "",
                        "Conversation History:",
                        *[
                            f"{message.role.capitalize()}: {message.content}"
                            for message in history
                        ],
                    ]
                )

            parts.extend(
                [
                    "",
                    "User Request:",
                    request.user_prompt,
                    "",
                    "Generate the best possible output.",
                ]
            )

            return "\n".join(parts).strip()
        except Exception as exc:  # pragma: no cover - defensive guard
            raise PromptBuildError("Failed to build prompt") from exc


class PromptBuilder(TelegramPromptBuilder):
    """Backwards-compatible default prompt builder."""
