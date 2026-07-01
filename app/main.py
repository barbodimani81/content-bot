from app.bot.telegram import TelegramBot


def main():
    bot = TelegramBot()
    bot.run()


if __name__ == "__main__":
    main()