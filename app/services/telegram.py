from telegram import Update
from app.services.content import generate_content
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from app.core.config import settings


class TelegramBot:
    def __init__(self):
        self.application = (
            Application.builder()
            .token(settings.telegram_bot_token)
            .build()
        )

        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(
            CommandHandler("start", self.start_command)
        )
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
            )

    async def start_command(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        await update.message.reply_text(
            "Siktir baba"
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        result = await generate_content(update.message.text)

        await update.message.reply_text(result["text"])

    def run(self):
        print("Telegram bot is running...")
        self.application.run_polling()