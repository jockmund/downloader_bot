from aiogram import types

from functions import *
from keyboards.inline import new_url_keyboard

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    from urllib.parse import urlparse
    if not urlparse(message.text).scheme:
        await message.answer(
            "Введена не корректная ссылка или ссылка отсутствует. Введите ссылку на понравившееся Вам видео.")
        return

    try:
        url_download = take_download_link(message.text)

        from pyshorteners import Shortener
        url = Shortener().tinyurl.short(url_download)
    except:
        await message.answer(
            "Введена не корректная ссылка или ссылка отсутствует. Введите ссылку на понравившееся Вам видео.")
        return

    await message.answer(f"Ваша ссылка для скачивания видео: {url}")

    await message.answer(f"Желаете скачать еще видео?", reply_markup=new_url_keyboard)
