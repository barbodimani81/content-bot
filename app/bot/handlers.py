from telegram import Update
from telegram.ext import ContextTypes

from app.core.container import orchestrator
from app.core.logging import logger


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None or not update.message.text:
        return

    user_id = update.effective_user.id if update.effective_user else None

    try:
        result = await orchestrator.generate(
            update.message.text,
            user_id=user_id,
        )
    except Exception:
        logger.exception("Failed to generate content")
        await update.message.reply_text(
            "Sorry, I couldn’t generate a response right now."
        )
        return

    await update.message.reply_text(result.text)
