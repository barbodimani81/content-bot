from app.orchestrators import ContentOrchestrator
from app.services import ContentService, HistoryService, PromptBuilder
from app.providers.llm.gemini import GeminiProvider

orchestrator = ContentOrchestrator(
    prompt_builder=PromptBuilder(),
    content_service=ContentService(GeminiProvider()),
    history_service=HistoryService(),
)