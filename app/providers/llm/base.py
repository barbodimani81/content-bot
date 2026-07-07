from abc import ABC, abstractmethod
from collections.abc import AsyncIterator


class BaseLLMProvider(ABC):
    provider_name: str = "base"

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate a complete response for the given prompt."""

    async def stream(self, prompt: str) -> AsyncIterator[str]:
        """Stream response chunks when a provider supports it."""
        raise NotImplementedError(
            f"{self.provider_name} does not support streaming yet"
        )
