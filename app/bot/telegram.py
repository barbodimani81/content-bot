from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.core.config import get_settings
from app.bot.commands import start_command, help_command
from app.bot.handlers import handle_message
from app.core.exceptions import ConfigurationError
from app.core.logging import configure_logging, logger


class TelegramBot:
    def __init__(self):
        configure_logging()
        settings = get_settings()

        if not settings.telegram_bot_token:
            raise ConfigurationError("TELEGRAM_BOT_TOKEN is not configured")

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
        logger.info("Telegram bot is running")
        self.application.run_polling()
