from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
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

    async def start_command(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        await update.message.reply_text(
            "Siktir baba"
        )

    def run(self):
        print("Telegram bot is running...")
        self.application.run_polling()