from dataclasses import dataclass
from typing import Dict


def generate_content(user_input: str) -> Dict:
    """
    MVP content generator (no LLM yet).
    """

    return {
        "text": f"migam siktir kon",
        "platform": "telegram",
        "meta": {
            "version": "v1",
            "source": "mock"
        }
    }