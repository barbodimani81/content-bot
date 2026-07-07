import unittest
from unittest.mock import AsyncMock

from app.orchestrators.content import ContentOrchestrator
from app.schemas.content import ContentResponse


class DummyPromptBuilder:
    def build(self, request, history=None):
        self.request = request
        self.history = history
        return "prompt"


class DummyContentService:
    def __init__(self):
        self.generate = AsyncMock(
            return_value=ContentResponse(text="result", platform="telegram")
        )


class DummyHistoryService:
    def __init__(self):
        self.get_messages = AsyncMock(return_value=[])
        self.add_user_message = AsyncMock()
        self.add_assistant_message = AsyncMock()


class OrchestratorTests(unittest.IsolatedAsyncioTestCase):
    async def test_generate_uses_dependencies(self):
        prompt_builder = DummyPromptBuilder()
        content_service = DummyContentService()
        history_service = DummyHistoryService()
        orchestrator = ContentOrchestrator(
            prompt_builder=prompt_builder,
            content_service=content_service,
            history_service=history_service,
        )

        response = await orchestrator.generate("hello", user_id=42)

        self.assertEqual(response.text, "result")
        self.assertEqual(prompt_builder.request.user_prompt, "hello")
        history_service.add_user_message.assert_awaited_once()
        history_service.add_assistant_message.assert_awaited_once()
        content_service.generate.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
