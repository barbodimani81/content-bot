import unittest

from app.schemas.content import ContentRequest, ConversationMessage
from app.services.prompt_builder import PromptBuilder


class PromptBuilderTests(unittest.TestCase):
    def test_build_includes_request_fields(self):
        builder = PromptBuilder()
        request = ContentRequest(user_prompt="Write a launch post")

        prompt = builder.build(request)

        self.assertIn("Platform: telegram", prompt)
        self.assertIn("User Request:", prompt)
        self.assertIn("Write a launch post", prompt)

    def test_build_includes_history(self):
        builder = PromptBuilder()
        request = ContentRequest(user_prompt="Continue")
        history = [ConversationMessage(role="user", content="Hello")]

        prompt = builder.build(request, history=history)

        self.assertIn("Conversation History:", prompt)
        self.assertIn("User: Hello", prompt)


if __name__ == "__main__":
    unittest.main()
