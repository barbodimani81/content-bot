from app.db import get_session_factory
from app.orchestrators import ContentOrchestrator
from app.providers.llm import build_llm_provider
from app.repositories import SqlAlchemyHistoryRepository
from app.services import ContentService, HistoryService, PromptBuilder


def build_orchestrator(provider_name: str | None = None) -> ContentOrchestrator:
    provider = build_llm_provider(provider_name)
    session_factory = get_session_factory()
    history_repository = (
        SqlAlchemyHistoryRepository(session_factory)
        if session_factory is not None
        else None
    )
    return ContentOrchestrator(
        prompt_builder=PromptBuilder(),
        content_service=ContentService(provider),
        history_service=HistoryService(history_repository),
    )


orchestrator = build_orchestrator()
