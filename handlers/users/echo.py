from aiogram import types
from functions import *

from loader import dp

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):

    formats = take_format_video(message.text)

    

    await message.answer(f"Ваша ссылка для скачивания: {message.text}")