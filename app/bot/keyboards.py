from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "Instagram",
                callback_data="instagram",
            )
        ],
        [
            InlineKeyboardButton(
                "kose ammat",
                callback_data="kose ammat",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)