from app.bot.telegram import TelegramBot
from app.core.exceptions import ConfigurationError
from app.core.logging import configure_logging, logger


def main():
    configure_logging()

    try:
        bot = TelegramBot()
    except ConfigurationError:
        logger.exception("Bot configuration is invalid")
        raise

    bot.run()


if __name__ == "__main__":
    main()
