import unittest

from app.core.exceptions import ProviderUnavailableError
from app.providers.llm import GeminiProvider, GrokProvider, build_llm_provider


class ProviderFactoryTests(unittest.TestCase):
    def test_build_default_provider(self):
        provider = build_llm_provider("gemini")

        self.assertIsInstance(provider, GeminiProvider)

    def test_build_grok_provider(self):
        provider = build_llm_provider("grok")

        self.assertIsInstance(provider, GrokProvider)

    def test_unknown_provider_raises(self):
        with self.assertRaises(ProviderUnavailableError):
            build_llm_provider("unknown")


if __name__ == "__main__":
    unittest.main()
