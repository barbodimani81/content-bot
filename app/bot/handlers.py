from telegram import Update
from telegram.ext import ContextTypes

from app.services.content import generate_content

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    result = await generate_content(
        update.message.text
    )

    await update.message.reply_text(
        result["text"]
    )