from app.schemas import ContentRequest, ContentResponse
from app.services import ContentService, HistoryService, PromptBuilder


class ContentOrchestrator:
    def __init__(
        self,
        prompt_builder: PromptBuilder,
        content_service: ContentService,
        history_service: HistoryService,
    ) -> None:
        self.prompt_builder = prompt_builder
        self.content_service = content_service
        self.history_service = history_service

    async def generate(
        self,
        user_input: str,
        user_id: int | None = None,
    ) -> ContentResponse:
        request = self._create_request(user_input, user_id=user_id)
        history = []

        if user_id is not None:
            history = list(await self.history_service.get_messages(user_id))
            await self.history_service.add_user_message(user_id, user_input)

        prompt = self._build_prompt(request, history=history)
        response = await self._generate_content(prompt, request.platform)

        if user_id is not None:
            await self.history_service.add_assistant_message(user_id, response.text)

        return response

    def _create_request(
        self,
        user_input: str,
        user_id: int | None = None,
    ) -> ContentRequest:
        return ContentRequest(
            user_prompt=user_input,
            platform="telegram",
            language="en",
            tone="professional",
            content_type="text",
            user_id=user_id,
        )

    def _build_prompt(
        self,
        request: ContentRequest,
        history=None,
    ) -> str:
        return self.prompt_builder.build(request, history=history)

    async def _generate_content(
        self,
        prompt: str,
        platform: str,
    ) -> ContentResponse:
        return await self.content_service.generate(prompt, platform=platform)

    async def stream_generate(
        self,
        user_input: str,
        user_id: int | None = None,
    ):
        request = self._create_request(user_input, user_id=user_id)
        history = []

        if user_id is not None:
            history = list(await self.history_service.get_messages(user_id))
            await self.history_service.add_user_message(user_id, user_input)

        prompt = self._build_prompt(request, history=history)

        async for chunk in self.content_service.stream(prompt):
            yield chunk
