from app.services.content import ContentService


class ContentOrchestrator:
    def __init__(self) -> None:
        self.content_service = ContentService()

    async def generate(self, user_input: str) -> dict:
        return await self.content_service.generate(user_input)
        