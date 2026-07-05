from app.schemas import ContentRequest


class PromptBuilder:
    def build(
        self,
        request: ContentRequest,
    ) -> str:
        return f"""
You are an expert AI content creator.

Platform:
{request.platform}

Language:
{request.language}

Tone:
{request.tone}

Content Type:
{request.content_type}

User Request:
{request.user_prompt}

Generate the best possible output.
""".strip()