from collections.abc import Sequence
from typing import Protocol

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from app.models.history import ConversationEntry
from app.schemas.content import ConversationMessage


class HistoryRepository(Protocol):
    async def list_messages(self, user_id: int) -> Sequence[ConversationMessage]:
        ...

    async def append_message(
        self,
        user_id: int,
        message: ConversationMessage,
    ) -> None:
        ...


class SqlAlchemyHistoryRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self.session_factory = session_factory

    async def list_messages(self, user_id: int) -> Sequence[ConversationMessage]:
        with self.session_factory() as session:
            rows = session.scalars(
                select(ConversationEntry)
                .where(ConversationEntry.user_id == user_id)
                .order_by(ConversationEntry.created_at.asc(), ConversationEntry.id.asc())
            ).all()

        return tuple(
            ConversationMessage(role=row.role, content=row.content, created_at=row.created_at)
            for row in rows
        )

    async def append_message(
        self,
        user_id: int,
        message: ConversationMessage,
    ) -> None:
        with self.session_factory() as session:
            session.add(
                ConversationEntry(
                    user_id=user_id,
                    role=message.role,
                    content=message.content,
                    created_at=message.created_at,
                )
            )
            session.commit()
