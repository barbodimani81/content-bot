from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from app.core.config import settings
from app.bot.commands import start_command, help_command
from app.bot.handlers import handle_message


class TelegramBot:
    def __init__(self):
        self.application = (
            Application.builder()
            .token(settings.telegram_bot_token)
            .build()
        )

        self.register_handlers()

    def register_handlers(self):
        self.application.add_handler(
            CommandHandler("start", start_command)
        )

        self.application.add_handler(
            CommandHandler("help", help_command)
        )

        # self.application.add_handler(
        #     CallbackQueryHandler(handle_callback)
        # )

        self.application.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                handle_message,
            )
        )

    def run(self):
        print("Telegram bot is running...")
        self.application.run_polling()