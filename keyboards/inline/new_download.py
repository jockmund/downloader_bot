from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

new_url_callback = CallbackData("choice", "answer")

new_url_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=new_url_callback.new(answer="yes"))
        ]
    ]
)