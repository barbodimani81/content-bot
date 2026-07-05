from app.schemas import ContentRequest
from app.services import ContentService, HistoryService, PromptBuilder

from app.schemas import ContentResponse

class ContentOrchestrator:
    def __init__(
        self,
        prompt_builder: PromptBuilder,
        content_service: ContentService,
        history_service: HistoryService,
    ):
        self.prompt_builder = prompt_builder
        self.content_service = content_service
        self.history_service = history_service

    async def generate(

        self,

        user_input: str,

    ) -> ContentResponse:

        request = self._create_request(user_input)

        prompt = self._build_prompt(request)

        response = await self._generate_content(prompt)

        return response

    def _create_request(

        self,

        user_input: str,

    ) -> ContentRequest:

        return ContentRequest(

            user_prompt=user_input,

            platform="telegram",

            language="en",

            tone="professional",

            content_type="text",

        )

    def _build_prompt(

        self,

        request: ContentRequest,

    ) -> str:

        return self.prompt_builder.build(request)

    async def _generate_content(

        self,

        prompt: str,

    ) -> ContentResponse:

        return await self.content_service.generate(prompt)
