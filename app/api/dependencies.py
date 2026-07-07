from functools import lru_cache

from app.core.container import build_orchestrator
from app.orchestrators.content import ContentOrchestrator


@lru_cache(maxsize=1)
def get_orchestrator() -> ContentOrchestrator:
    return build_orchestrator()
