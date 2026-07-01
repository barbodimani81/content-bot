from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import main_menu_keyboard


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "ye kosi begu sohbat konim",
        reply_markup=main_menu_keyboard(),
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
/start
/help

yekisho entekhab kon dige kiri
"""
    )