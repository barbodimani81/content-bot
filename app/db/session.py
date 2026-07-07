from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

_engine: Engine | None = None
_session_factory: sessionmaker[Session] | None = None


def get_engine() -> Engine | None:
    global _engine
    if _engine is not None:
        return _engine

    settings = get_settings()
    if not settings.database_url:
        return None

    _engine = create_engine(settings.database_url, future=True)
    return _engine


def get_session_factory() -> sessionmaker[Session] | None:
    global _session_factory
    if _session_factory is not None:
        return _session_factory

    engine = get_engine()
    if engine is None:
        return None

    _session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return _session_factory


def get_db_session() -> Iterator[Session]:
    session_factory = get_session_factory()
    if session_factory is None:
        raise RuntimeError("DATABASE_URL is not configured")

    session = session_factory()
    try:
        yield session
    finally:
        session.close()
