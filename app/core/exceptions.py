class ContentBotError(Exception):
    """Base exception for application-level failures."""


class ConfigurationError(ContentBotError):
    """Raised when the app is missing required runtime configuration."""


class PromptBuildError(ContentBotError):
    """Raised when a prompt cannot be assembled."""


class ProviderError(ContentBotError):
    """Raised when an LLM provider fails."""


class ProviderUnavailableError(ProviderError):
    """Raised when the selected LLM provider is not available."""


class GenerationError(ProviderError):
    """Raised when text generation fails unexpectedly."""


class HistoryError(ContentBotError):
    """Raised when conversation history cannot be loaded or saved."""
