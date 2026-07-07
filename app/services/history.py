from collections.abc import Sequence

from app.core.exceptions import HistoryError
from app.repositories.history import HistoryRepository
from app.schemas.content import ConversationMessage


class InMemoryHistoryRepository:
    def __init__(self) -> None:
        self._messages: dict[int, list[ConversationMessage]] = {}

    async def list_messages(self, user_id: int) -> Sequence[ConversationMessage]:
        return tuple(self._messages.get(user_id, ()))

    async def append_message(
        self,
        user_id: int,
        message: ConversationMessage,
    ) -> None:
        self._messages.setdefault(user_id, []).append(message)


class HistoryService:
    def __init__(self, repository: HistoryRepository | None = None) -> None:
        self.repository = repository or InMemoryHistoryRepository()

    async def get_messages(self, user_id: int) -> Sequence[ConversationMessage]:
        try:
            return await self.repository.list_messages(user_id)
        except Exception as exc:  # pragma: no cover - defensive guard
            raise HistoryError("Failed to load conversation history") from exc

    async def add_user_message(self, user_id: int, content: str) -> None:
        await self._append(user_id, "user", content)

    async def add_assistant_message(self, user_id: int, content: str) -> None:
        await self._append(user_id, "assistant", content)

    async def _append(self, user_id: int, role: str, content: str) -> None:
        try:
            await self.repository.append_message(
                user_id,
                ConversationMessage(role=role, content=content),
            )
        except Exception as exc:  # pragma: no cover - defensive guard
            raise HistoryError("Failed to save conversation message") from exc
