from telegram import Update
from telegram.ext import ContextTypes

from app.orchestrators.content import ContentOrchestrator

orchestrator = ContentOrchestrator()


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    result = await orchestrator.generate(
        update.message.text,
    )

    await update.message.reply_text(
        result["text"],
    )